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
                        stash expire time(seconds)
```

## Example
- 全てのclientを1日(86400秒)の間stash
```
$ python sensu-stash-scripy.py -u http://localhost:4567 -a -e 86400
```

- adminホストを1時間(3600秒)の間stash
```
$ python sensu-stash-scripy.py -u http://localhost:4567 -n www -e 3600
```

- adminホストとwwwホストを12時間(43200秒)の間stash
```
$ python sensu-stash-scripy.py -u http://localhost:4567 -n www,admin -e 43200
```
