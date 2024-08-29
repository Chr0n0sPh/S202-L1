from pymongo import MongoClient
class ProductAnalyzer:

    # Retorna o total de vendas por dia
    def total_vendas_por_dia(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {
                "_id": "$data_compra",
                "total_vendas": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}
            }},
            {"$sort": {"_id": 1}}
        ]