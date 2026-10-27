import { useState } from "react";
import { PRODUCTS } from "./data";
import ProductCard from "./components/ProductCard";
import ProductDetails from "./components/ProductDetails";

function App() {
  const [query, setQuery] = useState("");
  const [category, setCategory] = useState("all");
  const [selected, setSelected] = useState(null);

  const categories = [
    "all",
    ...new Set(PRODUCTS.map((product) => product.category)),
  ];

  const visible = PRODUCTS.filter((product) => {
    const matchesQuery = product.name
      .toLowerCase()
      .includes(query.toLowerCase());

    const matchesCategory =
      category === "all" || product.category === category;

    return matchesQuery && matchesCategory;
  });

  if (selected) {
    return (
      <ProductDetails
        product={selected}
        onBack={() => setSelected(null)}
      />
    );
  }

  return (
    <main>
      <h1>Katalog produktów</h1>

      <input
        type="text"
        placeholder="Szukaj produktu..."
        value={query}
        onChange={(event) => setQuery(event.target.value)}
      />

      <select
        value={category}
        onChange={(event) => setCategory(event.target.value)}
      >
        {categories.map((name) => (
          <option key={name} value={name}>
            {name === "all" ? "wszystkie kategorie" : name}
          </option>
        ))}
      </select>

      <div className="grid">
        {visible.map((product) => (
          <ProductCard
            key={product.id}
            product={product}
            onSelect={setSelected}
          />
        ))}
      </div>

      {visible.length === 0 && <p>Nic nie pasuje do wyszukiwania.</p>}
    </main>
  );
}

export default App;