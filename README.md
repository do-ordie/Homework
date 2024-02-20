The code is a sait
< form action="/twit" method="POST">
<label for="name">ИМЯ:</label>
<input type="text" id="name" name = "name"><br>
<input type="submit" value="Send">
</form>


<label for="name">Name (4 to 8 characters):</label>
<input type="text" id="name" name="name" required minlength="4" maxlength="8" size="10" />

<form method="POST" action="/twit">
        <input class="name" name="name" placeholder="Введите ваше имя">
    </form>

    <p><label>Twit: </label><input type="text" name="twit" value=""requied/>