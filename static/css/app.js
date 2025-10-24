const categories = [
  {name:"Авто", icon:"bi-car-front"},
  {name:"Недвижимость", icon:"bi-house-door"},
  {name:"Работа", icon:"bi-briefcase"},
  {name:"Одежда, обувь, аксессуары", icon:"bi-bag"},
  {name:"Хобби и отдых", icon:"bi-controller"},
  {name:"Животные", icon:"bi-paw"},
  {name:"Готовый бизнес и оборудование", icon:"bi-building"},
  {name:"Услуги", icon:"bi-tools"},
  {name:"Электроника", icon:"bi-phone"},
  {name:"Для дома и дачи", icon:"bi-lamp"},
  {name:"Запчасти", icon:"bi-gear"},
  {name:"Товары для детей", icon:"bi-emoji-smile"},
  {name:"Жильё для путешествия", icon:"bi-globe"},
  {name:"Красота и здоровье", icon:"bi-heart"}
];

const subcategories = {
  "Авто":["Автомобили","Мотоциклы","Скутеры","Грузовики","Водный транспорт"],
  "Недвижимость":["Квартиры","Дома","Участки","Аренда"],
  "Работа":["Вакансии","Резюме"],
  "Одежда, обувь, аксессуары":["Женская одежда","Мужская одежда","Обувь","Аксессуары","Сумки"],
  "Хобби и отдых":["Спорт","Игры","Книги","Туризм","Музыка"],
  "Животные":["Собаки","Кошки","Птицы","Рыбы","Грызуны"],
  "Готовый бизнес и оборудование":["Продажа бизнеса","Оборудование","Франшизы"],
  "Услуги":["Ремонт","Образование","Красота","Доставка"],
  "Электроника":["Телефоны","Компьютеры","Планшеты","Телевизоры","Аудио и видео"],
  "Для дома и дачи":["Мебель","Инструменты","Сад и огород","Освещение"],
  "Запчасти":["Автозапчасти","Мотозапчасти","Комплектующие для техники"],
  "Товары для детей":["Игрушки","Одежда","Коляски","Товары для школы"],
  "Жильё для путешествия":["Отели","Апартаменты","Хостелы","Квартиры посуточно"],
  "Красота и здоровье":["Косметика","Парфюмерия","Средства гигиены","Фитнес и здоровье"]
};

const catSection=document.getElementById("categories");
const subContainer=document.getElementById("subContainer");
categories.forEach(cat=>{
  const div=document.createElement("div");
  div.className="category";
  div.innerHTML=`<i class="bi ${cat.icon}"></i><h3>${cat.name}</h3>`;
  catSection.appendChild(div);

  div.addEventListener("mouseenter",()=>{
    const subs=subcategories[cat.name];
    if(!subs) return;
    subContainer.innerHTML="";
    subs.forEach(sub=>{
      const subItem=document.createElement("div");
      subItem.innerText=sub;
      subItem.addEventListener("click",e=>{
        e.stopPropagation();
        alert(`Вы выбрали: ${sub}`);
      });
      subContainer.appendChild(subItem);
    });
    const rect=div.getBoundingClientRect();
    subContainer.style.top=rect.bottom+window.scrollY+"px";
    subContainer.style.left=rect.left+window.scrollX+"px";
    subContainer.classList.add("show");
  });
});

document.addEventListener("click",e=>{
  if(!e.target.closest(".category")) subContainer.classList.remove("show");
});

async function loadAds(){
  try{
    const res=await fetch("ads.json");
    const ads=await res.json();
    const container=document.getElementById("adsContainer");
    container.innerHTML='<h2>Последние объявления</h2>';
    ads.forEach(ad=>{
      const div=document.createElement("div");
      div.className="ad";
      div.innerHTML=`<div class="ad-title">${ad.title}</div>
                     <div class="ad-price">${ad.price} ${ad.currency}</div>
                     <div class="ad-date">${ad.date}</div>
                     <div class="ad-user">От: ${ad.user}</div>`;
      container.appendChild(div);
    });
  }catch(err){console.log("Ошибка загрузки ads.json:",err);}
}

loadAds();
