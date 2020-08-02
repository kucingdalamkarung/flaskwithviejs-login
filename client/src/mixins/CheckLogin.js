export default {
    methods: {
        checkLogin() {
            if(localStorage.getItem('isLoggesIn'))
                return true

            return false
        }
    }
}