import pymongo

myclient = pymongo.MongoClient("mongodb://172.16.4.44:27017/")

# # 输出数据库
# dblist = myclient.list_database_names()
# for db in dblist:
#     print(db)

# 指定数据库
mydb = myclient["runoobdb"]

# # 所有集合
# collist = mydb.list_collection_names()
# for collect in collist:
#     print(collect)

# 指定集合
mycol = mydb["sites"]

# # 插入集合
# mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
#
# x = mycol.insert_one(mydict)
# print(x)

# # 批量插入
# mylist = [
#     {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
#     {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
#     {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
#     {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
#     {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
# ]
#
# x = mycol.insert_many(mylist)
# # 输出插入的所有文档对应的 _id 值
# print(x.inserted_ids)

# # 查询一个
# x = mycol.find_one()
#
# print(x)

# # 查询全部
# for x in mycol.find():
#   print(x)


# # 查询指定字段的数据
# for x in mycol.find({}, {"_id": 0, "name": 1, "alexa": 1}):
#     print(x)


# # 高级查询
# myquery = {"name": {"$gt": "H"}}
# mydoc = mycol.find(myquery).limit(3)
#
# for x in mydoc:
#     print(x)


# # 修改数据
# myquery = {"alexa": "10000"}
# newvalues = {"$set": {"alexa": "12345"}}
#
# mycol.update_one(myquery, newvalues)
#
# # 输出修改后的  "sites"  集合
# for x in mycol.find():
#     print(x)


# # 删除数据
# myquery = {"name": "Taobao"}
#
# mycol.delete_one(myquery)
#
# # 删除后输出
# for x in mycol.find():
#     print(x)