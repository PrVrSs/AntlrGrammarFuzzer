### example config for MySQL, mode fuzzing_sql_forms

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

### example config for TSQL, mode random_query
```
[antlr4_parser_setting]

sql_type = tsql
parser_file = grammar/antlr4/tsql/TSqlParser.g4
lexer_file = grammar/antlr4/tsql/TSqlLexer.g4

[original_parser_setting]

[antlr4_parser_setting]

sql_type = tsql
parser_file = grammar/antlr4/tsql/TSqlParser.g4
lexer_file = grammar/antlr4/tsql/TSqlLexer.g4

[original_parser_setting]

user = sa
password = mypass
host = localhost
database = SampleDB
error_info = false

[fuzzing_setting]
multiplication_scale = 2
random_scale = 2
mutate_mode = true
mutate_chance = 4
fuzzing_mode = random_query
start_grammar_rule = sql_clause
position_type = custom_range
count_to_generate = 2000

[print_setting]

print_mode = 4
print_in_file = false
file_name = log_brut.txt
print_in_console = true
```