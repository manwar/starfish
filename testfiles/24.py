def mkhtaccessfile (reviewersdir, reviewerid, reviewername, reviewerlogin):
    from constantsNew import chairlogin, passwdfilename, groupfilename, maintainerlogin
    allowedusers = maintainerlogin + " " + chairlogin
    filename = reviewersdir + `reviewerid` + '/' + '.htaccess'
    file = openforwrite (filename)
    file.lock('w|')
    #<? echo "s = \"\"\"\\\nAuthType Basic\n".
    # '';
    #!>
    Some_code_continuation

def mkhtaccessfile (reviewersdir, reviewerid, reviewername, reviewerlogin):
    from constantsNew import chairlogin, passwdfilename, groupfilename, maintainerlogin
    allowedusers = maintainerlogin + " " + chairlogin
    filename = reviewersdir + `reviewerid` + '/' + '.htaccess'
    file = openforwrite (filename)
    file.lock('w|')
    #<? echo "s = \"\"\"\\\nAuthType Basic\n".
    # '';
    #!>#+
s = """\
AuthType Basic

    #-
some code continuation
