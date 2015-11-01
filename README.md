# im-demo
Using sockjs &amp; nsq &amp; flask &amp; mysql, implement a im demo.

## HTTP APIs

#### GET  /inbox
Fetch threads list

+ offset {int}: Page number
+ limit {int}: Page size

Response

```
{
  "paging": {
    "prev": //,
    "next": //,
    "has_next": //
  },
  "data": [
    {
      "id": // Thread id, type is string,
      "message": {
        "sender": // Sender info,
        "receiver": // Receiver info,
        "content": // Message content, type is string
      },
      "is_read": // Has read or not, type is int
    }
  ]
}
```

#### GET  /inbox/<thread_id>

Get detail message in a thread.

Response:

```
{
  "paging": {
    "prev": //
    "next": //
    "has_next": //
  },
  "data": [
    {
      "id": // Message id, type is int,
      "sender": // Sender info,
      "receiver": // Receiver info,
      "content": // Message content, type is string
    }
  ]
}
```

#### PUT /inbox/<thread_id>

Set thread status to read.

```
{
  "success": True/False
}
```

Response

## Install Required

+ zc.buildout

```
pip install zc.buildout
```

## Setup

### Build
After you install `zc.buildout`, clone the source code, change directory to it,
execute command below:
```
buildout
```

### Install nsq
You can view install instruction [here](http://nsq.io/deployment/installing.html).

After everythings is ok, you can run

+ start im service

```
bin/im
```

+ start im api service

```
bin/im_apis
```

#####　You can via environment setting by

```
DEBUG=flask bin/im_apis
```
