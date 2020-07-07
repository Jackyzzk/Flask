let vm = new Vue({
    // vue对象接管了div
    el: '#app',
    data: {
        msg: 'hello vue!',
        sUrl: 'https://leetcode-cn.com/u/jackyzzk/',
        aList: [1, 2, 3, 4]
    },
    methods: {
        btn: function () {
            this.msg += ' click btn!';
        }
    }
});
