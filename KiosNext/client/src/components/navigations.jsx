import { Link } from "react-router-dom"
import Button from 'react-bootstrap/Button';

export function Navigations() {
  return (
    <div>
      <Link to="/Stockear">
        <Button variant="primary">Stockear</Button>
      </Link>
    </div>
  )
}