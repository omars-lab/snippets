#!/bin/bash

export ABC=123

function testing_if_paren_methods_can_see_exported_vars() (
  echo " <<< PAREN METHOD"
  echo $ABC
  echo "     PAREN METHOD >>>"
)

function testing_if_brace_methods_can_see_exported_vars() {
  echo " <<< BRACE METHOD"
  echo $ABC
  echo "     BRACE METHOD >>>"
}

function exporting_from_braces() {
  echo " <<< EXPORTING FROM BRACES"
  export EE=ee
  echo "     EXPORTING FROM BRACES >>>"
}

function exporting_from_paren() (
  echo " <<< EXPORTING FROM PARENS"
  export NN=nn
  echo "     EXPORTING FROM PARENS >>>"
)

function reading_from_braces_in_braces() {
  echo " <<< READING FROM BRACES IN BRACES"
  echo $EE
  echo "     READING FROM BRACES IN BRACES >>>"
}

function reading_from_parens_in_braces() {
  echo " <<< READING FROM PARENS IN BRACES"
  echo $NN
  echo "     READING FROM PARENS IN BRACES >>>"
}

function reading_from_braces_in_parens() (
  echo " <<< READING FROM BRACES IN BRACES"
  echo $EE
  echo "     READING FROM BRACES IN BRACES >>>"
)

function reading_from_parens_in_parens() (
  echo " <<< READING FROM PARENS IN PARENS"
  echo $NN
  echo "     READING FROM PARENS IN PARENS >>>"
)

testing_if_paren_methods_can_see_exported_vars
testing_if_brace_methods_can_see_exported_vars
exporting_from_braces
exporting_from_paren
reading_from_braces_in_braces
reading_from_parens_in_braces
reading_from_braces_in_parens
reading_from_parens_in_parens
