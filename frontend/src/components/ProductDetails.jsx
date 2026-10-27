import { formatPrice } from "../format";

function ProductDetails({ product, onBack }) {
  return (
    <article className="details">
      <button onClick={onBack}>&larr; Wróć do listy</button>

      <h1>{product.name}</h1>
      <p>{product.description}</p>
      <p className="price">{formatPrice(product.price)}</p>
      <p>Kategoria: {product.category}</p>
      <p>Na stanie: {product.stock} szt.</p>
    </article>
  );
}

export default ProductDetails;