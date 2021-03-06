# dbgen-model-template
A cookiecutter template for a dbgen model repo


## Simple Model 
### Quick Start
```
cookiecutter https://github.com/modelyst/dbgen-model-template --directory simple
```
### Options
 - `repo_name`: The name of the parent directory of the model (which will most likely be initialized to a git repo)
 - `model_name`: The name of the model and the python module that dbgen will import from 
 - `version`: The starting semantic version for this codebase
 - `database_dsn`: The postgresql DSN to be written to the default dotenv file (.env) in the repo. This can be changed at anytime and it is advised that the raw password is not written directly here for any systems other than for local testing. Please see the DBgen configuration options for passing secret credentials to dbgen securely.   
 - `clean`: A boolean indicating whether the example scripts should be written to the repo for reference. Default: True
 


# Tutorials 

## Alice and Bob Lab
### Quick Start
```
cookiecutter https://github.com/modelyst/dbgen-model-template --directory tutorials/alice_bob_lab
```
### Options
 - `repo_name`: The name of the parent directory of the model (which will most likely be initialized to a git repo)
 - `model_name`: The name of the model and the python module that dbgen will import from 
 - `version`: The starting semantic version for this codebase
 - `database_dsn`: The postgresql DSN to be written to the default dotenv file (.env) in the repo. This can be changed at anytime and it is advised that the raw password is not written directly here for any systems other than for local testing. Please see the DBgen configuration options for passing secret credentials to dbgen securely.   
 
