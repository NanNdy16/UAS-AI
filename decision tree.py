# Import library
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# 1. Membaca dataset
df = pd.read_excel(r"D:\Nanda\AI\Dataset.xlsx")
print(df.head())

# 2. Menambahkan label kategori penjualan: Tinggi atau Rendah
median_penjualan = df["Penjualan (pcs)"].median()
df["Kategori Penjualan"] = df["Penjualan (pcs)"].apply(
    lambda x: "Tinggi" if x >= median_penjualan else "Rendah"
)

# 3. Menentukan fitur dan label
features = df[["Kegiatan", "Curah Hujan (mm)"]]  # X
labels = df["Kategori Penjualan"]               # y

# 4. Membuat model Decision Tree dengan kriteria entropy (seperti ID3)
model = DecisionTreeClassifier(criterion="entropy", random_state=42)

# 5. Melatih model
model.fit(features, labels)

# 6. Visualisasi pohon keputusan
plt.figure(figsize=(17, 10))
plot_tree(model, feature_names=features.columns, class_names=model.classes_, filled=True)
plt.title("Pohon Keputusan: Prediksi Kategori Penjualan")
plt.show(block=True)
plt.show()
