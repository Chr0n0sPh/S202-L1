from database import Database
from helper.writeAJson import writeAJson
from analyzer import ProductAnalyzer

db = Database(database="mercado", collection="compras")
#db.resetDatabase()

# 1- Retorne o total de vendas por dia
# result = db.collection.aggregate([
#             {"$unwind": "$produtos"},
#             {"$group": {
#                 "_id": "$data_compra",
#                 "total_vendas": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}
#             }},
#             {"$sort": {"_id": 1}}
#         ])
#
# writeAJson(result, "Total de vendas por dia")

# 2 - Retorne o produto mais vendido em todas as compras.
# result = db.collection.aggregate([
#             {"$unwind": "$produtos"},
#             {"$group": {
#                 "_id": "$produtos.descricao",
#                 "total_quantidade": {"$sum": "$produtos.quantidade"}
#             }},
#             {"$sort": {"total_quantidade": -1}},
#             {"$limit": 1}
#         ])
# writeAJson(result, "Produto mais vendido em todas as compras")

# 3 - Encontre o cliente que mais gastou em uma única compra.
# result = db.collection.aggregate([
#             {"$unwind": "$produtos"},
#             {"$group": {
#                 "_id": "$cliente_id",
#                 "total_gasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}
#             }},
#             {"$sort": {"total_gasto": -1}},
#             {"$limit": 1}
#         ])
#
# writeAJson(result, "Cliente que mais gastou")

#4 - Liste todos os produtos que tiveram uma quantidade vendida acima de 1 unidades.
result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {
                "_id": "$produtos.descricao",
                "total_quantidade": {"$sum": "$produtos.quantidade"}
            }},
            {"$match": {"total_quantidade": {"$gt": 1}}},
            {"$sort": {"total_quantidade": -1}}
        ])

writeAJson(result, "Produtos com mais de uma venda")
# 1- Média de gasto total:
#result = db.collection.aggregate([
#    {"$unwind": "$produtos"},
#    {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
#    {"$group": {"_id": None, "media": {"$avg": "$total"}}}
#])
#
#writeAJson(result, "Média de gasto total")

# 2- Cliente que mais comprou em cada dia:
#result = db.collection.aggregate([
#     {"$unwind": "$produtos"},
#     {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
#     {"$sort": {"_id.data": 1, "total": -1}},
#     {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
#])
#
#writeAJson(result, "Cliente que mais comprou em cada dia")

# 3- Produto mais vendido:
#result = db.collection.aggregate([
#    {"$unwind": "$produtos"},
#    {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
#    {"$sort": {"total": -1}},
#    {"$limit": 1}
#])

#writeAJson(result, "Produto mais vendido")