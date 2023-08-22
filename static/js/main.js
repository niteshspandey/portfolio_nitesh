

function cracklogicblogposts() {
    fetch('https://cracklogic.com/wp-json/wp/v2/posts?_embed/')
        .then(res => res.json())
        .then(data => {
            const cracklogicposts = document.querySelector('.cracklogicblogposts')

            data.map(post => {
                cracklogicposts.innerHTML += `
                                    <a href="${post.link}" target="_blank">
                                    <div class="bg-slate-700 overflow-hidden rounded">
                                        <div class="">
                                            <img src="${post.yoast_head_json.og_image[0].url}" alt="" class="w-full h-[200px] object-cover">
                                        </div>
                                        <div class="px-4 py-4">
                                            <h2 class="text-xl truncate">${post.title.rendered}</h2>
                                        </div>
                                    </div>
                                    </a>
                                        `
            })

        })
}

window.onload = cracklogicblogposts()

function technocutterblogposts() {
    fetch('https://technocutter.com/wp-json/wp/v2/posts?_embed/')
        .then(res => res.json())
        .then(data => {
            const technocutterposts = document.querySelector('.technocutterblogposts')

            data.map(post => {
                technocutterposts.innerHTML += `
                                    <a href="${post.link}" target="_blank">
                                    <div class="bg-slate-700 overflow-hidden rounded">
                                        <div class="">
                                            <img src="${post.yoast_head_json.og_image[0].url}" alt="" class="w-full object-cover">
                                        </div>
                                        <div class="px-4 py-4">
                                            <h2 class="text-xl truncate">${post.title.rendered}</h2>
                                        </div>
                                    </div>
                                    </a>
                                        `
            })

        })
}

window.onload = technocutterblogposts()