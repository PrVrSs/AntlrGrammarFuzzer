# Fuzzer for parsers which are created with Antlr4 parser generator 

## Getting started

### Fast Installation

### Manual ANTLR Installation

`1`. Install Java (version 1.6 or higher):

```
sudo apt install default-jdk
```

`2.` Install ANTLR:

Download and copy:

```
cd /usr/local/lib
wget http://www.antlr.org/download/antlr-4.7-complete.jar
export CLASSPATH=".:/usr/local/lib/antlr-4.7-complete.jar:$CLASSPATH"
alias antlr4='java -jar /usr/local/lib/antlr-4.7-complete.jar'
alias grun='java org.antlr.v4.gui.TestRig'
```

### Python

`0.` virtual environment

````
sudo apt install python3.6-venv
mkdir ~/project
cd ~/project
python3.6 -m venv env
source env/bin/activate
````


`1.` Install Python runtime:

```
pip install wheel
pip install antlr4-python3-runtime
```

`2.` Install dev packages:

```
git clone https://github.com/PrVrSs/AntlrGrammarFuzzer
cd AntlrGrammarFuzzer
pip install -r requirements.txt
```

`3.` create a Python lexer or parser
```
cd path_to_project/grammar/antlr4/XSQL/
antlr4 -Dlanguage=Python3 XSLQGrammar.g4
```
or

```
java -jar /usr/local/lib/antlr-4.7-complete.jar -Dlanguage=Python3 XSLQGrammar.g4
```

### Testing
```
py.test
```

### Example 

```
original: True antlr: True sentence: SELECT *,TABLES.* INTO @AZ9.,VARIABLES LIMIT 0,1;
original: True antlr: True sentence: SELECT DATE.* INTO YEAR,@AZ9.;
original: True antlr: True sentence: SELECT SQL_CALC_FOUND_ROWS ALL * INTO OUTFILE "" LINES STARTING BY "\\9";
original: True antlr: True sentence: SELECT SQL_SMALL_RESULT *,VARIABLES.* INTO `UTF8MB4`,`3`;
```


