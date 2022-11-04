import { html, render } from "../lib/lit-html.js";
import { Router } from "../lib/vaadin-router.js";
import { router } from "../index.js";
import { boxesByPharm } from "../pharms/pharmStore.js";
import { removeBox } from "./boxStore.js";

export default class BoxList extends HTMLElement {

    constructor() {
        super();
    }

    getRoot() {
        return this;
        // return this.attachShadow({ mode: 'open' });
    }

    connectedCallback() {
        const { location } = router;
        this.id = location.params.pharm;
        this.loadAndRenderBoxes(this.id);
    }

    disconnectedCallback() {
    }

    loadAndRenderBoxes(id){
        boxesByPharm(id).then(data => {
            this.data = data;
            render(this.renderView(), this.getRoot());
        })
    }
    /*
    -------------------- eventi -------------------
    */

    onCreate(e, id) {
        e.preventDefault();
        Router.go(`/pharms/${id}/boxes/new`)
    }

    onEdit(e, id) {
        e.preventDefault();
        Router.go(`/boxes/${id}`)
    }


    onDelete(e, id) {
        e.preventDefault(); 
        removeBox(id)
        .then(resp => {
            this.loadAndRenderBoxes(this.id);
        });
        
    }

    /*
    --------------------render ---------------------
    */

    renderView() {
        return html`
            
            <h1 class="title has-text-centered">I tuoi boxes</h1>
            
            <div class="list">
                ${this.data.map(b => this.renderBox(b))}
            </div>

            <button @click = ${e => this.onCreate(e, this.id)} class="button is-primary">Nuovo</button>
        `;
    }

    renderBox(b) {
        return html`
            <div class="list-item">
                <div class="list-item-content">
                    <div class="list-item-title">${b.number}</div>
                    <div class="list-item-description">${b.color}</div>
                    <div class="list-item-description">${b.messagge}</div>
                    <div class="list-item-description">${b.timebox}</div>
                    <div class="list-item-description">${b.deltatime}</div>
                </div>

                <div class="list-item-controls">
                    <div class="buttons">
                        <button class="button is-warning" @click = ${e => this.onEdit(e, b.id)}>
                            <span class="icon is-small">
                            <i class="fas fa-edit"></i>
                            </span>
                            <span>Edit</span>
                        </button>
                        <button class="button is-danger" @click = ${e => this.onDelete(e, b.id)}>
                            <span class="icon is-small">
                            <i class="fas fa-trash"></i>
                            </span>
                            <span>Delete</span>
                        </button>
                    </div>
                </div>
            </div>
        `
    }
}

customElements.define("box-list", BoxList);