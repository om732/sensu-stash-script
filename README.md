# sensu-stash-script

## Usage
```
Usage: sensu-stash-script.py [options]

Options:
  -h, --help            show this help message and exit
  -u URL, --url=URL     request sensu api url
  -n NAME, --name=NAME  stash host name
  -a, --all             stash all host
  -e EXPIRE, --expire=EXPIRE
                        stash expire time
  -m MESSAGE, --message=MESSAGE
                        stashe reasone message
  -d, --delete          delete stash
```

## Example
### stash add
- 全てのclientを1日(86400秒)の間stash
```
$ python sensu-stash-scripy.py -u http://localhost:4567 -a -e 86400 -m "message"
```

- adminホストを1時間(3600秒)の間stash
```
$ python sensu-stash-scripy.py -u http://localhost:4567 -n www -e 3600 -m "message"
```

- adminホストとwwwホストを12時間(43200秒)の間stash
```
$ python sensu-stash-scripy.py -u http://localhost:4567 -n www,admin -e 43200 -m "message"
```

### stash delete
- 全てのclientのstashを削除
```
$ python sensu-stash-scripy.py -u http://localhost:4567 -a -d
```
