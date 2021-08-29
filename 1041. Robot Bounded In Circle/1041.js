/**
 * @param {string} instructions
 * @return {boolean}
 */
 var isRobotBounded = function(instructions) {
    let [dirX, dirY] = [0, 1]
    let [x, y] = [0, 0]
    
    for (const instruction of [...instructions]) {
        if (instruction === "G") {
            x += dirX
            y += dirY
        } else if (instruction === "L") {
            [dirX, dirY] = [-dirY, dirX]
        } else if (instruction === "R") {
            [dirX, dirY] = [dirY, -dirX]
        }
    }
    
    return (x ===0 && y===0) || dirY != 1 || dirX != 0
};