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
`4.` install MySQL
```
https://help.ubuntu.com/lts/serverguide/mysql.html
```
`5.` install TSQL
```
https://www.microsoft.com/en-us/sql-server/developer-get-started/python/ubuntu/
```
### Testing
```
py.test
```