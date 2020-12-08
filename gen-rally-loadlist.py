#!/usr/bin/python
# A tool to quickly generate large skip, load, xfail list for Rally in case of customized cloud policies
#
# How to use:
#   1. Prepare a list of testcases you want to include (e.g. rally verify show | grep failed > cases.list)
#   2. Prepare a complete list of testcases with ids (cd ~/.rally/verification/verifier-<uuid>; . .venv/bin/activate; cd repo; stestr list > ~/source/cvp-configuration/tempest/stestr.list)
#   3. Run this tool, use results.
#
cases = []
explanation = "Transition from the state Allowed to state Allowed is not allowed"
with open("cases.list", "rt") as f:
    cases = [x.replace("\n", "") for x in f.readlines()]
full_list = []
with open("stestr.list", "rt") as f:
    full_list = [x.replace("\n", "") for x in f.readlines()]
results = []
for case in cases:
    for id in full_list:
        if case in id:
           results.append(id + ": " + explanation)
           break
for id in results:
     print(id)
