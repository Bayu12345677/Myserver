#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cmath import pi
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

import os, sys, sqlite3, json

# buat tabel
def buat(nama):
    koneksi = sqlite3.connect("data.db")
    kursor = koneksi.cursor()
    kursor.execute(f"""CREATE TABLE IF NOT EXISTS {nama} (
        id INT PRIMARY KEY    NOT NULL,
        nama    TEXT   NOT NULL,
        key     INT NOT NULL,
        status  TEXT
    );""")
    koneksi.commit()


# menambahkan data pengguna
def buat_user(tabel, id, name, key, status):
    koneksi = sqlite3.connect("data.db")
    kursor = koneksi.cursor()
    kursor.execute(f"""INSERT INTO {tabel} (id, nama, key, status) VALUES (?, ?, ?, ?);""", (id, name, key, status))
    koneksi.commit()

# menghapus data pengguna
def hapus_user(tabel, id):
    koneksi = sqlite3.connect("data.db")
    kursor = koneksi.cursor()
    kursor.execute(f"""DELETE FROM {tabel} WHERE id = ?;""", (id,))
    koneksi.commit()

# buat edit data pengguna
def edit_user(tabel, id, name, key, status):
    koneksi = sqlite3.connect("data.db")
    kursor = koneksi.cursor()
    kursor.execute(f"""UPDATE {tabel} SET nama = ?, key = ?, status = ? WHERE id = ?;""", (name, key, status, id))
    koneksi.commit()

# menampilkan user yg tersimpan di data base

def tampil_user(tabel):
    koneksi = sqlite3.connect("data.db")
    kursor = koneksi.cursor()
    kursor.execute(f"""SELECT * FROM {tabel}""");
    # select = pencarian
    # * = semua
    # FROM = dari
    # tabel = tabel yg dituju
    data_isi = kursor.fetchall()
    return data_isi

@app.route('/api/create', methods=['POST'])
def create():
    if request.method == 'POST':
        data = request.get_json(force=True)
        if data['apikey'] == 'bayu': 
            buat_user(data['tabel'], data['id'], data['name'], data['key'], data['status'])
            return jsonify({'status': 'success', 'message': 'Data berhasil ditambahkan', 'id': data['id'], 'name': data['name'], 'key': data['key'], 'status': data['status']})
        else:
            return jsonify({'status': 'error','raise': 'apikey tidak valid'})
    else:
        return 'Error'

@app.route('/api/edit', methods=['POST'])
def edit():
    if request.method == 'POST':
        data = request.get_json(force=True)
        if data['apikey'] == 'bayu':
            edit_user(data['tabel'], data['id'], data['name'], data['key'], data['status'])
            return jsonify({'status': 'success','id': data['id'],'name': data['name'],'key': data['key'],'status': data['status']})
        else:
            return jsonify({'status': 'error','raise': 'apikey tidak valid'})
    else:
        return 'Error'

@app.route('/api/base/<tabel>/<apikey>', methods=['GET'])
def base(tabel, apikey):
    if request.method == 'GET':
        if apikey == 'bayu':
            buat(tabel)
            return jsonify({'status': 'success','tabel': tabel})
        else:
            return jsonify({'status': 'error','raise': 'apikey tidak valid'})
    else:
        return 'Error'

@app.route('/api/delete/<tabel>/<id>/<apikey>', methods=['GET'])
def delete(tabel, id, apikey):
    if request.method == 'GET':
        if apikey == 'bayu':
            hapus_user(tabel, id)
            return jsonify({'status': 'success','id': id})
        else:
            return jsonify({'status': 'error','raise': 'apikey tidak valid'})
    else:
        return 'Error'

@app.route('/api/show/<tabel>/<apikey>', methods=['GET'])
def show(tabel, apikey):
    if request.method == 'GET':
        if apikey == 'bayu':
            data = tampil_user(tabel)
            return(data)
        else:
            return jsonify({'status': 'error','raise': 'apikey tidak valid'})
    else:
        return 'Error'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)