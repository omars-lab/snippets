# engage-hld
Conceptual level design of Engage services modeled in pseudo code

![IMG](http://engage-beta.c1.io/plantuml/svg?
@startuml;
node "Kong API GW" as kong;
together {;
artifact "Engage API Stack" as engagestack {;
  node "Engage api" as engage;
  node "Engage schema" as engageschema;
  node "Engage Factors Needs" as factorsneeds;
  node "Kafka" as kafka;
  database "Mongo DB" as mongodb;
  cloud "NLP" as nlpref;
  engage -- engageschema;
  engage -- factorsneeds;
  engage -- mongodb;
  engage -- nlpref;
  engage -- kafka;
  nlpref .. nlpstack;
};
artifact "Engage UI Stack" as engageuistack {;
  node "Engage UI" as engageui;
  node "Cognitive Reference Store" as crs;
  cloud "Engage API" as engageref;
  engageui -- engageref;
  crs -- engageref;
  engageref .. engagestack;
};
artifact "NLP Stack" as nlpstack {;
  node "NLP API" as nlp;
  database "Neo4j" as neo4j;
  cloud "Corpus AWS db" as corpus;
  nlp -- neo4j;
  nlp .. corpus;
};
kong == engagestack;
kong == engageuistack;
};
@enduml
)

