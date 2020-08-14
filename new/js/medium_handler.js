window.onload = () => {
    let news_section = document.getElementById("news_section");
    let o_a_link = document.getElementById("o_a_link");
    let o_c_a_link = document.getElementById("o_c_a_link");
    let o_c_h_text = document.getElementById("o_c_h_text");
    let o_c_d_text = document.getElementById("o_c_d_text");
    let o_c_m_text = document.getElementById("o_c_m_text");
    let o_c_p_link = document.getElementById("o_c_p_link");

    let two_a_link = document.getElementById("two_a_link");
    let two_c_a_link = document.getElementById("two_c_a_link");
    let two_c_h_text = document.getElementById("two_c_h_text");
    let two_c_d_text = document.getElementById("two_c_d_text");
    let two_c_m_text = document.getElementById("two_c_m_text");
    let two_c_p_link = document.getElementById("two_c_p_link");

    let three_a_link = document.getElementById("three_a_link");
    let three_c_a_link = document.getElementById("three_c_a_link");
    let three_c_h_text = document.getElementById("three_c_h_text");
    let three_c_d_text = document.getElementById("three_c_d_text");
    let three_c_m_text = document.getElementById("three_c_m_text");
    let three_c_p_link = document.getElementById("three_c_p_link");

    fetch('https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/@cassandriel')
        .then((res) => res.json())
        .then((data) => {
            news_section.style.display = "block";
            o_a_link.setAttribute("href", data.items[0].link.toString());
            o_c_a_link.setAttribute("href", data.items[0].link.toString());
            o_c_p_link.setAttribute("href", data.items[0].link.toString());
            o_c_h_text.innerHTML = data.items[0].title.toString();
            o_c_d_text.innerHTML = data.items[0].pubDate.toString();
            let cont0 = data.items[0].content.replace(/<img[^>]*>/g,"");
            o_c_m_text.innerHTML =  cont0;
            
            //second card
            two_a_link.setAttribute("href", data.items[1].link.toString());
            two_c_a_link.setAttribute("href", data.items[1].link.toString());
            two_c_p_link.setAttribute("href", data.items[1].link.toString());
            two_c_h_text.innerHTML = data.items[1].title.toString();
            two_c_d_text.innerHTML = data.items[1].pubDate.toString();
            let cont1 = data.items[1].content.replace(/<img[^>]*>/g,"");
            two_c_m_text.innerHTML =  cont1;
            
            
            //third_card
            three_a_link.setAttribute("href", data.items[2].link.toString());
            three_c_a_link.setAttribute("href", data.items[2].link.toString());
            three_c_p_link.setAttribute("href", data.items[2].link.toString());
            three_c_h_text.innerHTML = data.items[2].title.toString();
            three_c_d_text.innerHTML = data.items[2].pubDate.toString();
            let cont2 = data.items[2].content.replace(/<img[^>]*>/g,"");
            three_c_m_text.innerHTML =  cont2;
        });
}