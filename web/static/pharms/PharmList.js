import configData from "./../config.js";
import { html, render } from "./../lib/lit-html.js";
import { Router } from "./../lib/vaadin-router.js";
import { removePharm } from "./pharmStore.js";
import { pharmsByUser } from "./../users/userStore.js"

export default class PharmList extends HTMLElement {

    constructor() {
        super();
    }

    getRoot() {
        return this;
        // return this.attachShadow({ mode: 'open' });
    }

    connectedCallback() {
        this.loadAndRenderPharms();
    }

    disconnectedCallback() {
    }

    loadAndRenderPharms(){
        pharmsByUser(configData.userId).then(data => {
            this.data = data;
            render(this.renderView(), this.getRoot());
        })
    }
    /*
    -------------------- eventi -------------------
    */

    onSelect(e, id) {
        e.preventDefault();
        Router.go(`/pharms/${id}/boxes`)
    }

    onCreate(e) {
        e.preventDefault();
        Router.go(`/createPharm`)
    }

    onEdit(e, id) {
        e.preventDefault();
        Router.go(`/pharms/${id}`)
    }

    onDelete(e, id) {
        e.preventDefault(); 
        removePharm(id)
        .then(resp => {
            this.loadAndRenderPharms();
        });
        
    }

    onTestEvent(e){
        e.preventDefault(); 
       const evt = new CustomEvent('blog-event',{
            detail:{
                category: 'prova'
            },
            bubbles: true
        })
        document.dispatchEvent(evt);
    }

    /*
    --------------------render ---------------------
    */

    renderView() {
        return html`
            
            <h1 class="title has-text-centered">Le tue Pharms</h1>
            
            <div class="list">
                ${this.data.map(p => this.renderPharm(p))}
            </div>

            <button @click = ${e => this.onCreate(e)} class="button is-primary">Nuovo</button>
            <button @click = ${e => this.onTestEvent(e)} class="button is-primary">CustomEvent</button>
        `;
    }

    renderPharm(p) {
        return html`
            <div class="list-item" @click = ${e => this.onSelect(e, p.id)}>
                <div class="list-item-content">
                    <div class="list-item-title">${p.name}</div>
                    <div class="list-item-description">${p.ip}</div>
                    <div class="list-item-description">${p.macaddress}</div>
                    <div class="list-item-description">${p.accesspoint}</div>
                </div>

                <div class="list-item-controls">
                    <div class="buttons">
                        <button class="button is-warning" @click = ${e => this.onEdit(e, p.id)}>
                            <span class="icon is-small">
                            <i class="fas fa-edit"></i>
                            </span>
                            <span>Edit</span>
                        </button>
                        <button class="button is-danger" @click = ${e => this.onDelete(e, p.id)}>
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

customElements.define("pharm-list", PharmList);