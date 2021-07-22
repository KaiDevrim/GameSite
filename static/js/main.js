const stars = document.getElementsByClassName("stars");
const star = "⭐️";

const times = document.getElementsByClassName("time");
for (let i = 0; i < stars.length; i++) {
  if (stars[i].innerHTML != "None") {
    const starsInt = parseInt(stars[i].innerHTML);
    totalStars = star.repeat(starsInt);
    stars[i].innerHTML = totalStars;
  } else {
    stars[i].innerHTML = "";
  }
}

for (let j = 0; j < times.length; j++) {
  const timesInt = parseInt(times[j].innerHTML);
  console.log(timesInt);
  if (timesInt >= 60) {
    const timeString = (timesInt % 60).toString();
    console.log(timeString);
    times[j].innerHTML = timeString + " Hours";
  } else if ((timesInt < 60 && timesInt > 1) || timesInt == 0) {
    times[j].innerHTML = timesInt.toString() + " Minutes";
  } else {
    times[j].innerHTML = timesInt.toString() + " Minute";
  }
}
