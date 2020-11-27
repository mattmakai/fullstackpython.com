title: Event Streams
category: page
slug: event-streams
sortorder: 1002
toc: False
sidebartitle: Event Streams
meta: An event stream is a log of one or more events.


Event streams are a log of one or more "things that happen", which are
usually referred to as events. Event streams are 
conceptually focused around things that happen rather than objects, 
which are the typical storage unit for 
[relational databases](/databases.html).

Apache Kafka and Gazette are a popular open source implementations of event 
streams. Amazon Web Services' Kinesis and 
[Azure Event-Hubs](https://azure.microsoft.com/en-us/services/event-hubs/)
are proprietary hosted implementations.


## How are event streams stored?
Some applications, such as aggregating millions of sensors, or thousands
of constantly streaming cameras, throw off large amounts of data. It's
difficult to process those large volumes of data in traditional data stores,
so event streams are built off of a simpler data structure: logs. 

Logs are ordered sequences of events and they typically have less constraints 
than a database. Logs can handle the high throughput writes needed to keep 
up with the constant flood of data from the source of an event stream.


## Event stream resources
* [What is Apache Kafka?](https://www.youtube.com/watch?v=FKgi3n-FyNU) sounds
  like it just focuses on Kafka but it actually covers the fundamental 
  concepts behind event streams and how they fit into 
  [microservices](/microservices.html) architectures.


