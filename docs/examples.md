* MySQL 
```
original: True antlr: True sentence: SELECT *,TABLES.* INTO @AZ9.,VARIABLES LIMIT 0,1;
original: True antlr: True sentence: SELECT DATE.* INTO YEAR,@AZ9.;
original: True antlr: True sentence: SELECT SQL_SMALL_RESULT *,VARIABLES.* INTO `UTF8MB4`,`3`;
```
* TSQL
```
original: True antlr: True sentence: CREATE MESSAGE TYPE XMLNAMESPACES AUTHORIZATION VALUE VALIDATION = WELL_FORMED_XML;
original: False antlr: False sentence: DISABLE TRIGGER , WORK . VAR ON DATABASE VAR DROP STATISTICS , VAR.VIEWS."3" ;;
original: True antlr: True sentence: ENABLE TRIGGER [3 3] . XML ON [3 3] . XMLNAMESPACES;
original: False antlr: False sentence: CREATE EXTERNAL RESOURCE POOL WORK WITH( MAX_CPU_PERCENT = 99 NUMANODE = , 99 99 MAXTRANSFER MAX_MEMORY_PERCENT = 99 )ASYMMETRIC XMLNAMESPACES;
```