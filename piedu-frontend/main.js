import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import ASide from './components/class/ASide.vue'
import Search from './components/class/Search.vue'
import NewClass from './components/class/NewClass.vue'
import ClassBox from './components/class/ClassBox.vue'
import Footer from './components/shared/Footer.vue'
import GoTopBtn from './components/shared/GoTopBtn.vue'

import HelpPage from './components/help/Page.vue'
import ContactPage from './components/contact/Page.vue'
import LoginContainer from './components/login/LoginContainer.vue'

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
Vue.use(VueAxios, axios)


new Vue({
    el: '#main-app',
    delimiters: ["[[", "]]"],
    // render: h => h(App)
    components: {
        NewClass, ASide, Search, ClassBox,
        'pi-footer': Footer,
        'go-top': GoTopBtn,
        'help-page': HelpPage,
        'contact-page': ContactPage,
        'login-container': LoginContainer
    },
    methods: {
    }

});
//
// function formdata_to_dict(formdata) {
//     let data = [];
//     for(var pair of formdata.entries()) {
//         data.push({'name':pair[0], 'value':pair[1]});
//     }
//     return data;
// }

