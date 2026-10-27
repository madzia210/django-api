import { formatPrice } from "../format";

function ProductCard({ product, onSelect }) {
  return (
    <article className="card" onClick={() => onSelect(product)}>
      <h2>{product.name}</h2>
      <p>{product.category}</p>
      <p className="price">{formatPrice(product.price)}</p>
    </article>
  );
}

export default ProductCard;