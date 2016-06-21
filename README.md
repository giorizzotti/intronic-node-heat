# OpenStack HEAT for IoTronic

This is an OpenStack HEAT plugin for the [IoTronic](https://github.com/MDSLab/iotronic) service in order to use the resources of its service function. It contains ```IoTronicNode.py``` to be copied in the heat plugins library and one yaml template: ```template.yaml``` to create an IoTronic Node.

## Prepare the plugin

* Create a heat plugin directory under /usr/lib and copy inside the file IoTronicNode.py (or place it alternatively under existing user-defined library):

```
mkdir /usr/lib/heat
cp src/IoTronicNode.py /usr/lib/heat/
```

* Uncomment the ```plugin_dirs``` line in ```/etc/heat/heat.conf``` and include the path to the library.

* Restart the heat engine service:

```
service openstack-heat-engine restart
```

* Run ```heat resource-type-list``` and verify that the following IoTronic resource shows up:

```
OS::IoTronic::Node
```

## Test the plugin

* Once the setup is done you can create the stack:

```heat stack-create [name_of_stack] --template-file=template.yaml``` 

* To check if the node was created:

```
iotronic node-list
```
