#!/bin/env python
#-*-coding:utf-8-*-

from optparse import OptionParser
from datetime import datetime
import time
import urllib
import urllib2
import json

now = int(time.mktime(datetime.now().timetuple()))

## apiへのアクセス
def request_api(url, data, delete = False):
    request = urllib2.Request(url)

    if delete:
        request.get_method = lambda: 'DELETE'

    if data:
        request.add_header('Content-Type', 'application/json')
        request.add_data(json.dumps(data))
    try:
        response = urllib2.urlopen(request)
        return response
    except urllib2.HTTPError, e:
        print e.code
        return False
    except urllib2.URLError, e:
        print e.reason
        return False

## clients一覧の取得
def get_clients(data):
    clients_list = []
    json_data = json.loads(data)
    for v in json_data:
        clients_list.append(v['name'])
    return clients_list

## stashesの実行
def main():
    parser = OptionParser()
    parser.add_option("-u", "--url",  dest="url",  default="http://localhost:4567", help="request sensu api url")
    parser.add_option("-n", "--name", dest="name", help="stash host name")
    parser.add_option("-a", "--all",  dest="all",  default=False, help="stash all host",  action="store_true")
    parser.add_option("-e", "--expire",  dest="expire", default=300, type="int", help="stash expire time")
    parser.add_option("-m", "--message",  dest="message", default="", type="string", help="stashe reasone message")
    parser.add_option("-d", "--delete",  dest="delete", default=False, help="delete stash", action="store_true")
    (options, args) = parser.parse_args()

    if options.all:
        result = request_api(options.url + '/clients', None)
        if result.code == 200:
            client_list = get_clients(result.read())
        else:
            print "error: connection failed to sensu api."
            exit()
    elif options.name:
        client_list = options.name.split(',')
    else:
        print "Arg error: need arg -a or -n [host name]"
        parser.print_help()
        exit()

    if client_list:
        for client in client_list:
            if options.delete:
                request_uri = '/stashes/silence/' + client
                request_client_data = {}
            else:
                request_uri = '/stashes'
                request_client_data = {}
                request_client_data['path'] = 'silence/' + client
                request_client_data['expire'] = options.expire
                request_client_data['content'] = {}
                request_client_data['content']['source'] = 'stash script'
                request_client_data['content']['reason'] = options.message
                request_client_data['content']['timestamp'] =now

            result = request_api(options.url + request_uri, request_client_data, options.delete)

            if result.code == 201 or result.code == 204:
                print "OK: " + client
            else:
                print "NG: " + client

if __name__ == '__main__':
    main()
