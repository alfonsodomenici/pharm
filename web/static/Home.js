import { html,render } from "./lib/lit-html.js";
export default class Home extends HTMLElement{
    constructor(){
        super();
    }

    getRoot(){
        return this;
    }

    connectedCallback(){
        render(this.renderView(),this.getRoot());
    }
    
    renderView(){
        return html`
            <section class="hero">
                <div class="hero-body">
                <p class="title">
                    Pharm App
                </p>
                <p class="subtitle">
                    Sviluppata con lit-html, vaadin-router, bulma.io e web-components
                </p>
                </div>
            </section>
        `;
    }
}
customElements.define("pharm-home", Home);