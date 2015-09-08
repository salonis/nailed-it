<!doctype html>
<html>
<title>Nailed It</title>
<!-- {% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello World!</h1>
{% endif %} -->
	<form method="POST">
		Name: 
		<input type="text" name="name">
		<br>
		Email (to contact you for confirmation and scheduling issues): 
		<input type="text" name="email">
		<br>
		<input type="radio" name="nailtype" value="plain" checked>Solid nails ($10)
		<br>
		<input type="radio" name="nailtype" value="dots">Polka dots ($15)
		<br>
		<input type="radio" name="nailtype" value="ombre">Ombre gradient nails ($25)
		<br><br>
		<input type="submit" value="Submit">
	</form>
</html>