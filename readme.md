# install

pip install --upgrade pip

pip uninstall antlr4-tools
pip install antlr4-tools

pip uninstall antlr4-python3-runtime
pip install antlr4-python3-runtime

# download pl/sql gramma
curl --output PlSqlLexer.g4 https://raw.githubusercontent.com/antlr/grammars-v4/master/sql/plsql/PlSqlLexer.g4
curl --output PlSqlParser.g4 https://raw.githubusercontent.com/antlr/grammars-v4/master/sql/plsql/PlSqlParser.g4

# convert gramma
antlr4 -Dlanguage=Python3 -o out Hello.g4
chmod 777 out/*.py

# test gramma
./test.py test.txt

# links

https://www.antlr.org
https://pypi.org/project/antlr-plsql
https://github.com/antlr/grammars-v4/blob/master/sql/plsql/Python3/PlSqlParserBase.py
https://alanhohn.com/posts/2016/antlr-python
https://faun.pub/introduction-to-antlr-python-af8a3c603d23
https://cucurbit.dev/posts/code-formatting-with-antlr-python
