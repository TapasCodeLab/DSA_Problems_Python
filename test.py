file = 'C:\\Users\\user\\Desktop\\test.rdb'
#content=b'REDIS0011\\xfa\\tredis-ver\\x057.2.0\\xfa\\nredis-bits\\xc0@\\xfe\\x00\\xfb\\x01\\x00\\x00\\tpineapple\\nstrawberry\\xff\\xec\\xe1~\\x8f\\xe02("\\n'
content=b'REDIS0011\xfa\tredis-ver\x057.2.0\xfa\nredis-bits\xc0@\xfe\x00\xfb\x01\x00\x00\tpineapple\nstrawberry\xff\xec\xe1~\x8f\xe02("\n'

with open(file, 'wb') as f:
    f.write(content)

with open(file, 'rb') as f:
    f.read()
    print(f)


