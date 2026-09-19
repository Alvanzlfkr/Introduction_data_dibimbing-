# Program Pengolahan Data Pesanan

## Deskripsi

Program ini dibuat menggunakan Python untuk mengelola data pesanan. Program memiliki dua class utama, yaitu `Order` dan `OrderProcessor`.

Class `Order` digunakan untuk menyimpan informasi setiap pesanan, seperti ID pesanan, nama pelanggan, tanggal pesanan, dan total harga. Class `OrderProcessor` digunakan untuk mengelola kumpulan pesanan, menghitung total pendapatan, serta menghitung total pajak dari seluruh pesanan.

Program dijalankan melalui file `main.py`, sedangkan class dipisahkan ke dalam file `order.py` dan `order_processor.py` agar kode lebih terstruktur dan mudah dikelola.

Pada class `Order`, terdapat:

- `order_id`
- `customer_name`
- `order_date`
- `total_amount`

disimpan sebagai atribut di dalam object.

Class `Order` juga memiliki method seperti:

- `calculate_tax()` untuk menghitung pajak pesanan.
- `display_order()` untuk menampilkan informasi pesanan.

Sementara itu, class `OrderProcessor` digunakan untuk mengelola kumpulan object `Order`. Class ini memiliki method seperti `add_order()`, `calculate_total_revenue()`, `calculate_total_tax()`, dan `display_order()`.

Dengan penerapan tersebut, data dan fungsi yang berkaitan dengan pesanan dikelompokkan ke dalam class masing-masing sehingga kode menjadi lebih terorganisir.

## Pengujian Program

Program diuji dengan memasukkan 3 data pesanan dengan total harga keseluruhan sebesar **Rp450.000**.

Dengan menggunakan tarif pajak sebesar **10%**, program secara otomatis menghitung total pajak:

**Rp450.000 × 10% = Rp45.000**

Hasil pengujian menunjukkan bahwa program berhasil menghitung total pendapatan sebesar **Rp450.000** dan total pajak sebesar **Rp45.000** secara otomatis.

### Contoh Output

```text
ID: 001
Name: Budi
Tanggal: 2024-01-01
Total: 100000

ID: 002
Name: Isal
Tanggal: 2024-01-02
Total: 200000

ID: 003
Name: Arfi
Tanggal: 2024-01-03
Total: 150000

Total Revenue: 450000
Total pajak: 45000
```
