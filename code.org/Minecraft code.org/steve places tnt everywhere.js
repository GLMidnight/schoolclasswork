for (var count3 = 0; count3 < 10; count3++) {
  moveForward();
  placeBlock("tnt");
  turnLeft();
  for (var count2 = 0; count2 < 10; count2++) {
      ifBlockAhead("water", function() {
      turnLeft();
    });
    moveForward();
    placeBlock("tnt");
    turnRight();
    for (var count = 0; count < 10; count++) {
          moveForward();
      ifBlockAhead("water", function() {
        turnLeft();
      });
      placeBlock("tnt");
    }
  }
