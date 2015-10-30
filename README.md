# im-demo
Using sockjs &amp; nsq &amp; flask &amp; mysql, implement a im demo.

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
```
bin/realtime_im
```
This command will start a sockjs server.
