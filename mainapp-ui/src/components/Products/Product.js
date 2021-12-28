import React, {useEffect, useState} from "react";
import axios from 'axios';
import { Link } from 'react-router-dom';
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Button from 'react-bootstrap/Button'
import Modal from 'react-bootstrap/Modal'



function ProductRange({ match }) {

    const [product, setProduct] = useState({})
    const id = match.params.id


    useEffect(() => {
        axios({
            method: "GET",
            url: `http://127.0.0.1:8000/api/product/${id}/`
        }).then(response => {
            setProduct(response.data)
        })
    }, [id])

    return (
            <Container>
            <Row>
                <Col sm={8}>
                    <h3 className="pb-4 mb-4 fst-italic border-bottom">
                    {product.name}
                    </h3>
                    <div className="row row-cols-1 row-cols-md-3">
                        <div className="col mb-4">
                            <div className="card h-100">
                                <img src={product.image} className="card-img-top" alt="..."/>
                                    <div className="card-body">
                                        <h5 className="card-title">{product.name}</h5>
                                        <p className="card-text">{product.description_1}</p>
                                    </div>
                            </div>
                        </div>
                    </div>

                </Col>
                <Col sm={4}>
                    <br/>
                    <div className="position-sticky" style={{"top":"2rem"}}>
                        <div className="p-4 mb-3 bg-light rounded">
                            <h4 className="fst-italic">About</h4>
                            <p className="mb-0">Customize this section to tell your visitors a little bit about your publication, writers, content, or something else entirely. Totally up to you.</p>
                        </div>
                    </div>
                </Col>
            </Row>
        </Container>




    )
}

export default ProductRange;