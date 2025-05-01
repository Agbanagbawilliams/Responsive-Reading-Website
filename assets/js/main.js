/*=============== SEARCH ===============*/
const searchButton = document.getElementById("search-button"),
  searchClose = document.getElementById("search-close"),
  searchContent = document.getElementById("search-content");
/*====== MENU SHOW =======*/
if (searchButton) {
  searchButton.addEventListener("click", () => {
    searchContent.classList.add("show-search");
  });
}
/*====== MENU HIDE =======*/
if (searchClose) {
  searchClose.addEventListener("click", () => {
    searchContent.classList.remove("show-search");
  });
}
/*=============== ADD SHADOW HEADER ===============*/
const shadowHeader = () => {
  const header = document.getElementById("header");
  // When scroll is greater than 50 viewport height, add the scroll-header class to header tag.
  this.scrollY >= 50
    ? header.classList.add("shadow-header")
    : header.classList.remove("shadow-header");
};
window.addEventListener("scroll", shadowHeader);
/*=============== HOME SWIPER ===============*/
let swiperHome = new Swiper(".home__swiper", {
  loop: true,
  spaceBetween: -24,
  grabCursor: true,
  slidesPerView: "auto",
  centeredSlides: "auto",

  autoplay: {
    delay: 3000,
    disableOnInteraction: false,
  },

  breakpoints: {
    1220: {
      spaceBetween: -32,
    },
  },
});
/*=============== FEATURED SWIPER ===============*/
let swiperFeatured = new Swiper(".featured__swiper", {
  loop: true,
  spaceBetween: 16,
  grabCursor: true,
  slidesPerView: "auto",
  centeredSlides: "auto",

  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },

  breakpoints: {
    1150: {
      slidesPerView: 3,
      centeredSlides: false,
    },
  },
});

/*=============== NEW SWIPER ===============*/
let swiperNew = new Swiper(".new__swiper", {
  loop: true,
  spaceBetween: 16,
  slidesPerView: "auto",

  breakpoints: {
    1150: {
      slidesPerView: 3,
    },
  },
});
/*=============== SHOW SCROLL UP ===============*/
const scrollUp = () => {
  const scrollUp = document.getElementById("scroll-up");
  // When scroll is higher than 350 viewport height, add the show-scroll class to the a tag with scrollup class.
  this.scrollY >= 350
    ? scrollUp.classList.add("show-scroll")
    : scrollUp.classList.remove("show-scroll");
};
window.addEventListener("scroll", scrollUp);
/*=============== SCROLL SECTIONS ACTIVE LINK ===============*/
const sections = document.querySelectorAll("section[id]");

const scrollActive = () => {
  const scrollDown = window.scrollY;

  sections.forEach((current) => {
    const sectionHeight = current.offsetHeight,
      sectionTop = current.offsetTop - 58,
      sectionId = current.getAttribute("id"),
      sectionClass = document.querySelector(
        `.nav__menu a[href*= ${sectionId}]`
      );
    if (scrollDown > sectionTop && scrollDown <= sectionTop + sectionHeight) {
      sectionClass.classList.add("active_link");
    } else {
      sectionClass.classList.remove("active_link");
    }
  });
};
window.addEventListener("scroll", scrollActive);
/*=============== SCROLL REVEAL ANIMATION ===============*/
const sr = ScrollReveal({
  origin: 'top',
  distance: '60px',
  duration: 2500,
  delay: 400,
 // reset: true repeat animations
})

sr.reveal(`.home__data, .featured__container, .new__container, .about__text, .footer`)
sr.reveal(`.home__images`, {delay: 600})
sr.reveal(`.about__img`, { origin: "left" });
sr.reveal(`.about__img-2`, { origin: "right" });

        // Fetch books from Flask API
        fetch('/api/books')
            .then(response => response.json())
            .then(books => {
                let container = document.getElementById('books-container');
                books.forEach(book => {
                    let bookDiv = document.createElement('div');
                    bookDiv.innerHTML = `
                        <h2>${book.title}</h2>
                        <p><strong>Author:</strong> ${book.author}</p>
                        <p>${book.description}</p>
                        <a href="${book.url}" target="_blank">Read More</a><br>
                        <img src="${book.image}" alt="${book.title}" width="150">
                        <hr>
                    `;
                    container.appendChild(bookDiv);
                });
            })
            .catch(error => console.error('Error fetching books:', error));
/*======================== LANG DROPDOWN MENU ====================*/
// API URL for LibreTranslate (self-hosted or the public instance)
const API_URL = 'https://libretranslate.com/translate';

// Function to toggle language dropdown menu visibility
function toggleLanguageMenu() {
  const menu = document.getElementById("languageMenu");
  menu.style.display = menu.style.display === "block" ? "none" : "block";
}

// Function to switch language and translate page content
function switchLanguage(lang) {
  alert("Language switched to: " + lang);

  // Collect all text nodes that need translation
  const elements = document.body.getElementsByTagName('*');
  let textNodes = [];
  for (let i = 0; i < elements.length; i++) {
    if (elements[i].childNodes.length) {
      for (let j = 0; j < elements[i].childNodes.length; j++) {
        if (elements[i].childNodes[j].nodeType === 3) {
          textNodes.push(elements[i].childNodes[j]);
        }
      }
    }
  }

  // Prepare the texts to translate
  const textsToTranslate = textNodes.map(node => node.textContent);

  // Construct the request body for LibreTranslate
  const requestBody = {
    q: textsToTranslate.join('\n'),
    source: 'en',
    target: lang
  };

  // Send the translation request to LibreTranslate
  fetch(API_URL, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(requestBody)
  })
    .then(response => response.json())
    .then(data => {
      if (data.error) {
        throw new Error('API Error: ' + data.error);
      }

      // Update the page content with translated text
      let counter = 0;
      textNodes.forEach(node => {
        if (data.translations[counter]) {
          node.textContent = data.translations[counter].translatedText;
          counter++;
        }
      });
    })
    .catch(error => {
      console.error('Error translating content:', error);
      alert("Translation failed. Please try again later.");
    });

  // Close the language menu after selection
  document.getElementById("languageMenu").style.display = "none";
}

// Close the menu if clicked outside
window.addEventListener("click", function (e) {
  if (!e.target.closest(".language-dropdown")) {
    document.getElementById("languageMenu").style.display = "none";
  }
});
