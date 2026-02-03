USE aurelia;

-- --------------------
-- USERS (10)
-- --------------------
INSERT INTO Users (name, email) VALUES
('Aurelia Weaver', 'aurelia@example.com'),
('Luna Vale', 'luna@example.com'),
('Seren Kade', 'seren@example.com'),
('Mira Solis', 'mira@example.com'),
('Eli Rowan', 'eli@example.com'),
('Nyx Calder', 'nyx@example.com'),
('Orin Frost', 'orin@example.com'),
('Calla Bloom', 'calla@example.com'),
('Theo Ash', 'theo@example.com'),
('Iris Wynn', 'iris@example.com');

-- --------------------
-- SYMBOLS (10)
-- --------------------
INSERT INTO Symbols (name, description) VALUES
('Water', 'Emotion and the unconscious'),
('Fire', 'Transformation and intensity'),
('Flight', 'Freedom or escape'),
('Falling', 'Loss of control or transition'),
('Mirror', 'Self-reflection or identity'),
('Forest', 'The unknown or inner world'),
('Moon', 'Intuition and hidden thoughts'),
('Cat', 'Independence and mystery'),
('Swan', 'Grace and metamorphosis'),
('Stars', 'Destiny and guidance');

-- --------------------
-- DREAMS (30)
-- --------------------
INSERT INTO Dreams (user_id, title, description, date, mood, vividness) VALUES
(1, 'Silver Lake', 'A lake reflecting constellations.', '2026-01-01', 'Calm', 7),
(2, 'Burning Staircase', 'Climbing stairs made of fire.', '2026-01-02', 'Anxious', 8),
(3, 'Glass Forest', 'Trees made of glass chimed in the wind.', '2026-01-03', 'Wonder', 9),
(4, 'Endless Library', 'Books stretched beyond the horizon.', '2026-01-04', 'Curious', 6),
(5, 'Falling Clock', 'Time fell apart into pieces.', '2026-01-05', 'Uneasy', 8),
(6, 'Moon Bridge', 'A bridge leading to the moon.', '2026-01-06', 'Peaceful', 7),
(7, 'Cathedral of Stars', 'A temple built from starlight.', '2026-01-07', 'Awe', 9),
(8, 'Ocean Train', 'A train crossing the sea.', '2026-01-08', 'Calm', 6),
(9, 'Mirror City', 'A city where every wall reflected me.', '2026-01-09', 'Confused', 7),
(10, 'Swan River', 'Swans guiding a river upstream.', '2026-01-10', 'Serene', 6),
(1, 'Ash Garden', 'Flowers grew from ash.', '2026-01-11', 'Melancholy', 7),
(2, 'Floating Market', 'Shops drifting in the sky.', '2026-01-12', 'Joyful', 8),
(3, 'Shadow Theater', 'Shadows performed a play.', '2026-01-13', 'Curious', 6),
(4, 'Crystal Rain', 'Rain fell like crystals.', '2026-01-14', 'Wonder', 9),
(5, 'Clockwork Birds', 'Metal birds sang at dawn.', '2026-01-15', 'Intrigued', 7),
(6, 'Golden Tide', 'The sea turned to gold.', '2026-01-16', 'Awe', 8),
(7, 'Stairway Down', 'Stairs led into clouds below.', '2026-01-17', 'Uneasy', 7),
(8, 'Paper Moon', 'The moon folded like origami.', '2026-01-18', 'Dreamy', 6),
(9, 'Sleeping City', 'Everyone slept at once.', '2026-01-19', 'Quiet', 5),
(10, 'Star Orchard', 'Stars grew on trees.', '2026-01-20', 'Joyful', 8),
(1, 'Whispering Lake', 'The water spoke in riddles.', '2026-01-21', 'Curious', 7),
(2, 'Fire Snow', 'Snowflakes burned softly.', '2026-01-22', 'Surreal', 9),
(3, 'Hidden Door', 'A door appeared in the sky.', '2026-01-23', 'Intrigued', 6),
(4, 'Vanishing Roads', 'Roads disappeared behind me.', '2026-01-24', 'Anxious', 7),
(5, 'Star Compass', 'A compass pointing to stars.', '2026-01-25', 'Hopeful', 8),
(6, 'Echo Garden', 'Voices bloomed like flowers.', '2026-01-26', 'Peaceful', 6),
(7, 'Moon Tides', 'The moon pulled the streets.', '2026-01-27', 'Surreal', 8),
(8, 'Cat in the Sky', 'A giant cat slept on clouds.', '2026-01-28', 'Amused', 7),
(9, 'Mirror Sea', 'The sea reflected another world.', '2026-01-29', 'Awe', 9),
(10, 'Falling Stars', 'Stars fell like rain.', '2026-01-30', 'Melancholy', 8);

-- --------------------
-- DREAMSYMBOLS (~60 links)
-- --------------------
INSERT INTO DreamSymbols (dream_id, symbol_id) VALUES
(1,1),(1,10),(2,2),(2,4),(3,6),(3,5),(4,5),(4,10),
(5,4),(5,10),(6,7),(6,3),(7,10),(7,7),(8,1),(8,3),
(9,5),(9,4),(10,9),(10,1),(11,2),(11,6),(12,3),(12,10),
(13,5),(13,7),(14,10),(14,1),(15,2),(15,8),(16,1),(16,10),
(17,4),(17,3),(18,7),(18,5),(19,5),(19,6),(20,10),(20,9),
(21,1),(21,7),(22,2),(22,1),(23,5),(23,3),(24,4),(24,6),
(25,10),(25,7),(26,6),(26,5),(27,7),(27,1),(28,8),(28,3),
(29,5),(29,1),(30,10),(30,4);

-- --------------------
-- POEMS (15)
-- --------------------
INSERT INTO Poems (author_id, dream_id, content, created_at) VALUES
(2, 1, 'Stars ripple under my feet; I do not fall.', NOW()),
(3, 3, 'Glass remembers every footstep of light.', NOW()),
(4, 4, 'Between shelves, I misplaced my name.', NOW()),
(5, 5, 'Time breaks like thin ice beneath thought.', NOW()),
(6, 6, 'I cross the moon and leave no shadow.', NOW()),
(7, 7, 'The sky learns architecture from our hope.', NOW()),
(8, 8, 'Steel sings when the sea listens.', NOW()),
(9, 9, 'Every mirror forgets me differently.', NOW()),
(10, 10, 'Swans write rivers with their silence.', NOW()),
(1, 11, 'Ash still remembers being a flower.', NOW()),
(2, 12, 'Markets drift where gravity goes to dream.', NOW()),
(3, 14, 'Rain keeps its promises in crystal.', NOW()),
(4, 18, 'The moon folds itself into my pocket.', NOW()),
(5, 21, 'The lake speaks, but only in questions.', NOW()),
(6, 30, 'Even falling stars get tired of falling.', NOW());
