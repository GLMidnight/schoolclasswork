for (var count12 = 0; count12 < 10; count12++) {
  moveForward();
  for (var count = 0; count < 10; count++) {
      placeBlock("planksBirch");
  }
  for (var count11 = 0; count11 < 3; count11++) {
      for (var count2 = 0; count2 < 3; count2++) {
          turnLeft();
    }
    for (var count3 = 0; count3 < 3; count3++) {
          moveForward();
      placeBlock("planksBirch");
      turnLeft();
      moveForward();
      placeBlock("planksBirch");
      turnRight();
      moveForward();
      placeBlock("planksBirch");
    }
    placeBlock("planksBirch");
    placeBlock("planksBirch");
    placeBlock("planksBirch");
    for (var count10 = 0; count10 < 9; count10++) {
          moveForward();
      turnLeft();
      placeBlock("planksBirch");
      moveForward();
      moveForward();
      turnRight();
      moveForward();
      placeBlock("planksBirch");
      for (var count5 = 0; count5 < 6; count5++) {
              moveForward();
        turnLeft();
        moveForward();
        placeBlock("planksOak");
        moveForward();
        turnRight();
        turnRight();
        moveForward();
        for (var count4 = 0; count4 < 7; count4++) {
                  moveForward();
          placeBlock("planksOak");
        }
        placeBlock("planksOak");
        turnRight();
      }
      for (var count9 = 0; count9 < 3; count9++) {
              moveForward();
        turnLeft();
        turnRight();
        placeBlock("planksSpruce");
        for (var count6 = 0; count6 < 5; count6++) {
                  turnRight();
        }
        for (var count7 = 0; count7 < 4; count7++) {
                  moveForward();
          placeBlock("planksSpruce");
        }
        for (var count8 = 0; count8 < 4; count8++) {
                  moveForward();
          placeBlock("wool");
        }
      }
    }
  }