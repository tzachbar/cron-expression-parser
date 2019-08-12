# cron-expression-parser
A utility class for parsing a cron job expression.

To run the parser: `python cron_parser.py <cron_expression>`<br />
example: `python cron_parser.py */5 1-3 * 8 * pwd`<br />
You will then see the printed parsed cron results

Syntax such as `@daily`, `@weekly`, ..., `@yearly` or `sun`, `mon`, ...  is not supported (yet) 


#### tests
To run all tests, run `pytest`<br />
Because pytest is a requirement for running tests, make sure you have it installed:<br /> 
`pip install -r requirements.txt`

#### troubleshooting
make sure your `PYTHONPATH` environment variable is set to the project's root working directory:<br />
`export PYTHONPATH=<project_root_dir>`