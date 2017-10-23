# Config file syntax

### Antlr4 Parser Setting

* sql_type - mysql / tsql
* parser_file - path to parser_file
* lexer_file - path to lexer_file

### Original Parser Setting

* user 
* password 
* host
* database
* error_info - true/false

### Fuzzing Setting

* multiplication_scale -
* random_scale - 
* mutate_mode = true/false
* mutate_chance - 
* fuzzing_mode = fuzzing_sql_forms / random_query
    1. fuzzing_sql_forms - brut SQLForms // TODO: add mode 2 Token
        * start_query 
        * insert_node_name
        * position_type = single / custom_range / default_range
            1. single
                * start_position = int 
            2. custom_range
                * start_position = int
                * end_position = int
            3. default range (not done)
        * count_to_generate   # summary generate count_to_generate * position count
    2. random_query - generate random query
        * start grammar rule
        * count_to_generate 
* sql_forms_file -  path to sql_forms_file

### Print Setting

* print_in_file = true/false
* file_name = *.txt
* print_in_console = true/false
* print_mode = 0 - 4
    * 0 - Antlr4 False / Original False
    * 1 - Antlr4 True / Original True
    * 2 - Antlr4 False / Original True
    * 3 - Antlr4 True / Original False
    * 4 - all(0 - 3)

## Example config file

### simple config
```
[antlr4_parser_setting]

sql_type = mysql
parser_file = grammar/antlr4/mysql/mysqlParser.g4
lexer_file = grammar/antlr4/mysql/mysqlLexer.g4
```

### example config

```
[antlr4_parser_setting]
sql_type = mysql
parser_file = grammar/antlr4/mysql/mysqlParser.g4
lexer_file = grammar/antlr4/mysql/mysqlLexer.g4

[original_parser_setting]
user = root
password = toor
host = 127.0.0.1
error_info = true

[fuzzing_setting]
multiplication_scale = 1
random_scale = 1
mutate_mode = false
mutate_chance = 1
fuzzing_mode = fuzzing_sql_forms
sql_forms_file = sql_forms/SelectForms.sql
start_query = 0
insert_node_name = querySpecification
position_type = custom_range
start_position = 0
end_position = 2
count_to_generate = 2
start_grammar_rule = root

[print_setting]
print_mode = 4
print_in_file = true
file_name = log_brut.txt
print_in_console = true
```


