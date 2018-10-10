from flask import Flask
from flask_restplus import Api, Resource, fields
import sys, os

from server.instance import server
from models.book import book

app, api = server.app, server.api

books_db = [
    {"id": 0, "title": "War and Peace"},
    {"id": 1, "title": "Python for Dummies"},
]

@api.route('/books')
class BookList(Resource):
    @api.marshal_list_with(book)
    def get(self):
        return books_db

    @api.expect(book)
    @api.marshal_with(book)
    def post(self):
        books_db.append(api.payload)
        return api.payload

@api.route('/books/<int:id>')
class Book(Resource):
    def find_one(self, id):
        return next((b for b in books_db if b["id"] == id), None)

    @api.marshal_with(book)
    def get(self, id):
        match = self.find_one(id)
        return match if match else ("Not found", 404)

    @api.marshal_with(book)
    def delete(self, id):
        global books_db 
        match = self.find_one(id)
        books_db = list(filter(lambda b: b["id"] != id, books_db))
        return match

    @api.expect(book)
    @api.marshal_with(book)
    def put(self, id):
        match = self.find_one(id)
        if match != None:
            match.update(api.payload)
            match["id"] = id
        return match

