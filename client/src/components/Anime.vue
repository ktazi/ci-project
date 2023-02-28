<template>
    <div class="container">
        <div class="banner">
                <h1 id="title" >
                WELCOME TO ANIME PREDICTIONS
                </h1>
        </div>
        <div class="content">
                <table border=1 align=left cellpadding="4" cellspacing="2" >
                    <tr>
                    <td nowrap class="subtitle" bgcolor= #9327bb>
                        <p>COOL WEBSITES</p>
                    </td>
                    </tr>
                    <tr>
                    <td nowrap bgcolor= #4823E7>
                        <a href=""><b>My magic blog</b></a>
                    </td>
                    </tr>
                    <tr>
                    <td nowrap bgcolor=#9327bb>
                        <a href="https://myanimelist.net/"><b>My anime list</b></a>
                    </td>
                    </tr>
                    <tr>
                    <td nowrap bgcolor=#4823E7>
                        <a href="https://www.crunchyroll.com/fr/"><b>Crunchyroll</b></a>
                    </td>
                    </tr>
                    <tr>
                    <td nowrap bgcolor=#9327bb>
                        <a href="https://www.amazon.fr/"><b>My amazon wishlist :3</b></a>
                    </td>
                    </tr>
                    <tr>
                    <td nowrap bgcolor=#4823E7>
                        <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><b>My youtube channel</b></a>
                    </td>
                    </tr>
                    <tr>
                    <td nowrap bgcolor=#9327bb>
                        <img src="../assets/edgy_anime_girl.png" width="290" >
                    </td>
                    </tr>
                </table>
            </div>
            <h1 id="title">今日は !!! Welcome to the magic anime website !!!</h1>
            <div class="content_container">
                <img src="../assets/sailor_moon.gif">

                <p>We can predict whether or not you will like an anime title !</p>
        
                <p>All you need to do is write some information on it and we'll do the magic  :3</p>

                <div>
                <ul>
                <li>
                    <label for="name">Anime title :</label>
                    <input type="text" id="name" name="name" v-model="anime_description.name" >
                </li>
                <li>
                    <label for="genres">Anime genres :</label>
                    <input type="text" id="genres" name="genres" v-model="anime_description.genre">
                </li>
                <li>
                    <label for="description">Anime description :</label>
                    <input type="text" id="description" name="description" v-model="anime_description.description">
                </li>
                <li>
                    <label for="type">Anime type :</label>
                    <input type="text" id="type" name="type" v-model="anime_description.type">
                </li>
                <li>
                    <label for="producer">Anime producer :</label>
                    <input type="text" id="producer" name="producer" v-model="anime_description.producer">
                </li>
                <li>
                    <label for="studio">Anime studio :</label>
                    <input type="text" id="studio" name="studio" v-model="anime_description.studio">
                </li>
                </ul> 
                </div>
                <button class="button-36" v-on:click="predict"> Predict </button>
                <h2> OUR PREDICTION IS : {{ message }}</h2>

            </div>

    </div>
  </template>
<style>

.subtitle{
    
font-family: 'Times New Roman', Times, bold;
color :white;
}
.banner{
    opacity: 0.8;
    border: double;
    background-size: 150px;
    background-image: url("../assets/anya_magnifique.png");
    background-repeat: repeat;
    margin-left: auto;
}
.content_container{
    font-family: "Lucida Console", "Courier New", monospace;
    padding-left: 25%;
}
#title{
    font-family: "Lucida Console", "Courier New", monospace;

    margin-left: 25%;
    color:blue
}
.content{
    color:black
}
a{
    color:aliceblue
}

/* CSS */
.button-36 {
  background-image: linear-gradient(92.88deg, #455EB5 9.16%, #5643CC 43.89%, #673FD7 64.72%);
  border-radius: 8px;
  border-style: none;
  box-sizing: border-box;
  color: #FFFFFF;
  cursor: pointer;
  flex-shrink: 0;
  font-family: "Inter UI","SF Pro Display",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Oxygen,Ubuntu,Cantarell,"Open Sans","Helvetica Neue",sans-serif;
  font-size: 16px;
  font-weight: 500;
  height: 4rem;
  padding: 0 1.6rem;
  text-align: center;
  text-shadow: rgba(0, 0, 0, 0.25) 0 3px 8px;
  transition: all .5s;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
}

.button-36:hover {
  box-shadow: rgba(80, 63, 205, 0.5) 0 1px 30px;
  transition-duration: .1s;
}

@media (min-width: 768px) {
  .button-36 {
    padding: 0 2.6rem;
  }
}
</style>

<script>
  import axios from 'axios';
  
  export default {
    name: 'Anime',
    data() {
      return {
        anime_description : {name : "", genre : "", description : "", type : "", producer : "", studio : ""},
        message : "..."
      };
    },
    methods: {
      
      predict(){
        const path = "http://localhost:5000/predict"
        axios.get(path, {params : this.anime_description})
        .then((res) =>{
          this.message = res.data
        }
        )
      }
      /*
      getMessage() {
        const path = 'http://localhost:5000/ping';
        axios.get(path)
          .then((res) => {
            this.msg = res.data;
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
      },*/
    },
    created() {
      //this.getMessage();
    },
  };
  </script>
  