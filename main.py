from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'The Lord of the Rings - The Fellowship of the Ring',
        'author' : 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'title': 'Don Quixote',
        'author' : 'Miguel de Cervantes'
    },
    {
        'id': 3,
        'title': 'Crime and Punishment',
        'author' : 'Fyodor Dostoevsky'
    }
]

@app.route('/books/ListAllBooks')
def list_all_books():
    list_books = [{'title': book['title'], 'author': book['author']} for book in books]
    return jsonify(list_books)

@app.route('/books/BookById',methods=['GET'])
def search_book_id():
    book_id = request.args.get('book_id', type=int)
    if book_id is None:
        return jsonify({'message': 'Parameter book_id not provided'}), 400
    else:
        for book in books:
            if book['id'] == book_id:
                return jsonify({'title': book['title'], 'author': book['author']})
            else:
                return jsonify({'message': 'Book not found'}), 404
            
@app.route('/books/ChangeBookById', methods=['PUT'])
def alter_book_id():
    book_id = request.args.get('book_id', type=int)
    book_found = next((returned_book for returned_book in books if returned_book ['id'] == book_id), None)
    if book_found is None:
        return jsonify({'message': 'Book not found'}), 404
    
    data = request.json
    if 'title' in data:
        book_found['title'] = data['title']
    if 'author' in data:
        book_found['author'] = data['author']
    
    return jsonify({'message': 'Book updated sucessfully', 'Book': {'title': book_found['title'], 'author': book_found['author']}})

@app.route('/books/DeleteBookById', methods=['DELETE'])
def delete_book_id():
    book_id = request.args.get('book_id', type=int)
    book_found = next((returned_book for returned_book in books if returned_book ['id'] == book_id), None)
    if book_found is None:
        return jsonify({'message': 'Book not found'}), 404
    else:
        books.remove(book_found)
        list_all = [{'title': book['title'], 'author': book['author']} for book in books]
        return jsonify({'message': 'Book removed sucessfully', 'books' : list_all}), 200


app.run(port=5000,host='localhost',debug=True)