#!/bin/bash

function print_message(){
  echo
  echo "************************************************"
  echo $1
  echo
}

function switch_to_virtual_env(){
  print_message "switching to virtual environment"
  pwd
  source "./venv/bin/activate"
}

function install_requirement_txt(){
  print_message "Updating pip"
  pip install --upgrade pip
  print_message "installing requirements"
  pip3 install -r ./requirements.txt
}

function make_virtual_environment(){
  print_message "making virtual environment"
  python3 -m venv ./venv
}

function install_pre_commit_hooks() {
    print_message "installing pre-commit hooks"
    pre-commit install
}

function create_or_switch_to_virtual_environment(){
  virtual_env_dir="./venv"
  if [ -d "$virtual_env_dir" ]
  then
    switch_to_virtual_env
    install_requirement_txt
    install_pre_commit_hooks
  else
    make_virtual_environment
    switch_to_virtual_env
    install_requirement_txt
    install_pre_commit_hooks
  fi
}

create_or_switch_to_virtual_environment
