import requtsts

res = requtsts.get('https://sendgrid.kke.co.jp/')
print(res.text)