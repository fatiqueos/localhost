<?php

$clientIP = $_SERVER['REMOTE_ADDR'];

header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');
header("Content-Type: application/json; utf-8;");

$baglanti = new mysqli('localhost', 'root', '', '101m');

if ($_SERVER["REQUEST_METHOD"] === "GET" && isset($_GET["tc"])) {
    $tc = $_GET["tc"];
    
    $sth = $baglanti->prepare("SELECT * FROM `101m` WHERE `TC` = ?");
    $sth->bind_param("s", $tc);
    $sth->execute();
    $result = $sth->get_result();
        $response = array(); // Yeni bir dizi oluştur

        if ($result->num_rows > 0) {
            while ($row = $result->fetch_assoc()) {
                $response[] = array(
                    "YAKINLIK" => "KENDİSİ",
                    "TC" => $row["TC"],
                    "ADI" => $row["ADI"],
                    "SOYADI" => $row["SOYADI"],
                    "DOGUMTARIHI" => $row["DOGUMTARIHI"],
                    "ANNEADI" => $row["ANNEADI"],
                    "ANNETC" => $row["ANNETC"],
                    "BABAADI" => $row["BABAADI"],
                    "BABATC" => $row["BABATC"],
                    "NUFUSIL" => $row["NUFUSIL"],
                    "NUFUSILCE" => $row["NUFUSILCE"]
                );
              $sqlcocugu = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["TC"] ."' OR `ANNETC` = '" . $row["TC"] ."' ) ";
              $resultcocugu = $baglanti->query($sqlcocugu);

              $sqlkardesi = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["BABATC"] ."' OR `ANNETC` = '" . $row["ANNETC"] ."' ) ";
              $resultkardesi = $baglanti->query($sqlkardesi);
              $sqlbabasi = "SELECT * FROM `101m` WHERE `TC` = '" . $row["BABATC"] ."' ";
              $resultbabasi = $baglanti->query($sqlbabasi);
              $sqlanasi = "SELECT * FROM `101m` WHERE `TC` = '" . $row["ANNETC"] ."' ";
              $resultanasi = $baglanti->query($sqlanasi);

              $sqlkendicocugu = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["TC"] ."' OR `ANNETC` = '" . $row["TC"] ."' ) ";
              $resultkendicocugu = $baglanti->query($sqlkendicocugu);
              while($row = $resultkendicocugu->fetch_assoc()) {
                $response[] = array(
                    "YAKINLIK" => "ÇOCUĞU",
                    "TC" => $row["TC"],
                    "ADI" => $row["ADI"],
                    "SOYADI" => $row["SOYADI"],
                    "DOGUMTARIHI" => $row["DOGUMTARIHI"],
                    "ANNEADI" => $row["ANNEADI"],
                    "ANNETC" => $row["ANNETC"],
                    "BABAADI" => $row["BABAADI"],
                    "BABATC" => $row["BABATC"],
                    "NUFUSIL" => $row["NUFUSIL"],
                    "NUFUSILCE" => $row["NUFUSILCE"]
                );
            
    
                  $sqlkendikendicocugu = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["TC"] ."' OR `ANNETC` = '" . $row["TC"] ."' ) ";
                  $resultkendikendicocugu = $baglanti->query($sqlkendikendicocugu);    
                  while($row = $resultkendikendicocugu->fetch_assoc()) {
                    $response[] = array(
                        "YAKINLIK" => "TORUNU",
                        "TC" => $row["TC"],
                        "ADI" => $row["ADI"],
                        "SOYADI" => $row["SOYADI"],
                        "DOGUMTARIHI" => $row["DOGUMTARIHI"],
                        "ANNEADI" => $row["ANNEADI"],
                        "ANNETC" => $row["ANNETC"],
                        "BABAADI" => $row["BABAADI"],
                        "BABATC" => $row["BABATC"],
                        "NUFUSIL" => $row["NUFUSIL"],
                        "NUFUSILCE" => $row["NUFUSILCE"]
                    );
                      $sqlkendikendikendicocugu = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["TC"] ."' OR `ANNETC` = '" . $row["TC"] ."' ) ";
                      $resultkendikendikendicocugu = $baglanti->query($sqlkendikendikendicocugu);    
                      while($row = $resultkendikendikendicocugu->fetch_assoc()) {
                         
                          
                      }
                  }
              }
              while($row = $resultkardesi->fetch_assoc()) {
                $response[] = array(
                    "YAKINLIK" => "KARDEŞ",
                    "TC" => $row["TC"],
                    "ADI" => $row["ADI"],
                    "SOYADI" => $row["SOYADI"],
                    "DOGUMTARIHI" => $row["DOGUMTARIHI"],
                    "ANNEADI" => $row["ANNEADI"],
                    "ANNETC" => $row["ANNETC"],
                    "BABAADI" => $row["BABAADI"],
                    "BABATC" => $row["BABATC"],
                    "NUFUSIL" => $row["NUFUSIL"],
                    "NUFUSILCE" => $row["NUFUSILCE"]
                );
                  $sqlkardescocugu = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["TC"] ."' OR `ANNETC` = '" . $row["TC"] ."' ) ";
                  $resultkardescocugu = $baglanti->query($sqlkardescocugu);
                  while($row = $resultkardescocugu->fetch_assoc()) {
                    $response[] = array(
                        "YAKINLIK" => "YEĞENİ",
                        "TC" => $row["TC"],
                        "ADI" => $row["ADI"],
                        "SOYADI" => $row["SOYADI"],
                        "DOGUMTARIHI" => $row["DOGUMTARIHI"],
                        "ANNEADI" => $row["ANNEADI"],
                        "ANNETC" => $row["ANNETC"],
                        "BABAADI" => $row["BABAADI"],
                        "BABATC" => $row["BABATC"],
                        "NUFUSIL" => $row["NUFUSIL"],
                        "NUFUSILCE" => $row["NUFUSILCE"]
                    );
                      
                      $sqlkardeskardescocugu = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["TC"] ."' OR `ANNETC` = '" . $row["TC"] ."' ) ";
                      $resultkardeskardescocugu = $baglanti->query($sqlkardeskardescocugu);    
                      while($row = $resultkardeskardescocugu->fetch_assoc()) {
                          
                          $sqlkardeskardeskardescocugu = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["TC"] ."' OR `ANNETC` = '" . $row["TC"] ."' ) ";
                          $resultkardeskardeskardescocugu = $baglanti->query($sqlkardeskardeskardescocugu);    
                          while($row = $resultkardeskardeskardescocugu->fetch_assoc()) {
                              
                              
                          }
                      }
                  }
  
              }
  
              while($row = $resultbabasi->fetch_assoc()) {
                $response[] = array(
                    "YAKINLIK" => "BABASI",
                    "TC" => $row["TC"],
                    "ADI" => $row["ADI"],
                    "SOYADI" => $row["SOYADI"],
                    "DOGUMTARIHI" => $row["DOGUMTARIHI"],
                    "ANNEADI" => $row["ANNEADI"],
                    "ANNETC" => $row["ANNETC"],
                    "BABAADI" => $row["BABAADI"],
                    "BABATC" => $row["BABATC"],
                    "NUFUSIL" => $row["NUFUSIL"],
                    "NUFUSILCE" => $row["NUFUSILCE"]
                );
                  $sqlbabakardesi = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["BABATC"] ."' OR `ANNETC` = '" . $row["ANNETC"] ."' ) ";
                  $resultbabakardesi = $baglanti->query($sqlbabakardesi);
                  $sqlbabababasi = "SELECT * FROM `101m` WHERE `TC` = '" . $row["BABATC"] ."' ";
                  $resultbabababasi = $baglanti->query($sqlbabababasi);
                  $sqlbabaanasi = "SELECT * FROM `101m` WHERE `TC` = '" . $row["ANNETC"] ."' ";
                  $resultbabaanasi = $baglanti->query($sqlbabaanasi);
  
                  while($row = $resultbabakardesi->fetch_assoc()) {
                    $response[] = array(
                        "YAKINLIK" => "AMCA/HALA",
                        "TC" => $row["TC"],
                        "ADI" => $row["ADI"],
                        "SOYADI" => $row["SOYADI"],
                        "DOGUMTARIHI" => $row["DOGUMTARIHI"],
                        "ANNEADI" => $row["ANNEADI"],
                        "ANNETC" => $row["ANNETC"],
                        "BABAADI" => $row["BABAADI"],
                        "BABATC" => $row["BABATC"],
                        "NUFUSIL" => $row["NUFUSIL"],
                        "NUFUSILCE" => $row["NUFUSILCE"]
                    );
                      $sqlbabakardescocugu = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["TC"] ."' OR `ANNETC` = '" . $row["TC"] ."' ) ";
                      $resultbabakardescocugu = $baglanti->query($sqlbabakardescocugu);
                      while($row = $resultbabakardescocugu->fetch_assoc()) {
                        $response[] = array(
                            "YAKINLIK" => "BABA TARAFI KUZEN",
                            "TC" => $row["TC"],
                            "ADI" => $row["ADI"],
                            "SOYADI" => $row["SOYADI"],
                            "DOGUMTARIHI" => $row["DOGUMTARIHI"],
                            "ANNEADI" => $row["ANNEADI"],
                            "ANNETC" => $row["ANNETC"],
                            "BABAADI" => $row["BABAADI"],
                            "BABATC" => $row["BABATC"],
                            "NUFUSIL" => $row["NUFUSIL"],
                            "NUFUSILCE" => $row["NUFUSILCE"]
                        );
                          $sqlbabakardesbabakardescocugu = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["TC"] ."' OR `ANNETC` = '" . $row["TC"] ."' ) ";
                          $resultbabakardesbabakardescocugu = $baglanti->query($sqlbabakardesbabakardescocugu);    
                          while($row = $resultbabakardesbabakardescocugu->fetch_assoc()) {
                             
                              $sqlbabakardesbabakardesbabakardescocugu = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["TC"] ."' OR `ANNETC` = '" . $row["TC"] ."' ) ";
                              $resultbabakardesbabakardesbabakardescocugu = $baglanti->query($sqlbabakardesbabakardesbabakardescocugu);    
                              while($row = $resultbabakardesbabakardesbabakardescocugu->fetch_assoc()) {
                                 
                                  
                              }
                          }

                      }
                  }
          
                      while($row = $resultbabababasi->fetch_assoc()) {
                        $response[] = array(
                            "YAKINLIK" => "DEDESİ",
                            "TC" => $row["TC"],
                            "ADI" => $row["ADI"],
                            "SOYADI" => $row["SOYADI"],
                            "DOGUMTARIHI" => $row["DOGUMTARIHI"],
                            "ANNEADI" => $row["ANNEADI"],
                            "ANNETC" => $row["ANNETC"],
                            "BABAADI" => $row["BABAADI"],
                            "BABATC" => $row["BABATC"],
                            "NUFUSIL" => $row["NUFUSIL"],
                            "NUFUSILCE" => $row["NUFUSILCE"]
                        );
                          $sqlbabakardesi = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["BABATC"] ."' OR `ANNETC` = '" . $row["ANNETC"] ."' ) ";
                          $resultbabakardesi = $baglanti->query($sqlbabakardesi);
                          $sqlbabababasi = "SELECT * FROM `101m` WHERE `TC` = '" . $row["BABATC"] ."' ";
                          $resultbabababasi = $baglanti->query($sqlbabababasi);
                          $sqlbabaanasi = "SELECT * FROM `101m` WHERE `TC` = '" . $row["ANNETC"] ."' ";
                          $resultbabaanasi = $baglanti->query($sqlbabaanasi);
          
                          while($row = $resultbabakardesi->fetch_assoc()) {
                            
                              $sqlbabababakardescocugu = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["TC"] ."' OR `ANNETC` = '" . $row["TC"] ."' ) ";
                              $resultbabababakardescocugu = $baglanti->query($sqlbabababakardescocugu);
                              while($row = $resultbabababakardescocugu->fetch_assoc()) {
                                 
                                  $sqlbabababakardesbabababakardescocugu = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["TC"] ."' OR `ANNETC` = '" . $row["TC"] ."' ) ";
                                  $resultbabababakardesbabababakardescocugu = $baglanti->query($sqlbabababakardesbabababakardescocugu);    
                                  while($row = $resultbabababakardesbabababakardescocugu->fetch_assoc()) {
                                      
                                      $sqlbabababakardesbabababakardesbabababakardescocugu = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["TC"] ."' OR `ANNETC` = '" . $row["TC"] ."' ) ";
                                      $resultbabababakardesbabababakardesbabababakardescocugu = $baglanti->query($sqlbabababakardesbabababakardesbabababakardescocugu);    
                                      while($row = $resultbabababakardesbabababakardesbabababakardescocugu->fetch_assoc()) {
                                         
                                          
                                      }
                                  }
                              }
                          }
              
                          while($row = $resultbabababasi->fetch_assoc()) {
                             
                          }

                      }
                      while($row = $resultbabaanasi->fetch_assoc()) {
                        $response[] = array(
                            "YAKINLIK" => "BABAANNESİ",
                            "TC" => $row["TC"],
                            "ADI" => $row["ADI"],
                            "SOYADI" => $row["SOYADI"],
                            "DOGUMTARIHI" => $row["DOGUMTARIHI"],
                            "ANNEADI" => $row["ANNEADI"],
                            "ANNETC" => $row["ANNETC"],
                            "BABAADI" => $row["BABAADI"],
                            "BABATC" => $row["BABATC"],
                            "NUFUSIL" => $row["NUFUSIL"],
                            "NUFUSILCE" => $row["NUFUSILCE"]
                        );
                          $sqlbabakardesi = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["BABATC"] ."' OR `ANNETC` = '" . $row["ANNETC"] ."' ) ";
                          $resultbabakardesi = $baglanti->query($sqlbabakardesi);
                          $sqlbabababasi = "SELECT * FROM `101m` WHERE `TC` = '" . $row["BABATC"] ."' ";
                          $resultbabababasi = $baglanti->query($sqlbabababasi);
                          $sqlbabaanasi = "SELECT * FROM `101m` WHERE `TC` = '" . $row["ANNETC"] ."' ";
                          $resultbabaanasi = $baglanti->query($sqlbabaanasi);
          
                          while($row = $resultbabakardesi->fetch_assoc()) {
                            
                              $sqlbabaannekardescocugu = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["TC"] ."' OR `ANNETC` = '" . $row["TC"] ."' ) ";
                              $resultbabaannekardescocugu = $baglanti->query($sqlbabaannekardescocugu);
                              while($row = $resultbabaannekardescocugu->fetch_assoc()) {
                                 
                                  $sqlbabaannekardesbabaannekardescocugu = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["TC"] ."' OR `ANNETC` = '" . $row["TC"] ."' ) ";
                                  $resultbabaannekardesbabaannekardescocugu = $baglanti->query($sqlbabaannekardesbabaannekardescocugu);    
                                  while($row = $resultbabaannekardesbabaannekardescocugu->fetch_assoc()) {
                                      
                                      $sqlbabaannekardesbabaannekardesbabaannekardescocugu = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["TC"] ."' OR `ANNETC` = '" . $row["TC"] ."' ) ";
                                      $resultbabaannekardesbabaannekardesbabaannekardescocugu = $baglanti->query($sqlbabaannekardesbabaannekardesbabaannekardescocugu);    
                                      while($row = $resultbabaannekardesbabaannekardesbabaannekardescocugu->fetch_assoc()) {
                                         
                                          
                                      }
                                  }
                              }

                          }
              
                          while($row = $resultbabababasi->fetch_assoc()) {
                             
                              
                          }
                          while($row = $resultbabaanasi->fetch_assoc()) {
                             
                              
                          }
  
                      }
                  }
              }
              while($row = $resultanasi->fetch_assoc()) {
                $response[] = array(
                    "YAKINLIK" => "ANNESİ",
                    "TC" => $row["TC"],
                    "ADI" => $row["ADI"],
                    "SOYADI" => $row["SOYADI"],
                    "DOGUMTARIHI" => $row["DOGUMTARIHI"],
                    "ANNEADI" => $row["ANNEADI"],
                    "ANNETC" => $row["ANNETC"],
                    "BABAADI" => $row["BABAADI"],
                    "BABATC" => $row["BABATC"],
                    "NUFUSIL" => $row["NUFUSIL"],
                    "NUFUSILCE" => $row["NUFUSILCE"]
                );
                  $sqlannekardesi = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["BABATC"] ."' OR `ANNETC` = '" . $row["ANNETC"] ."' ) ";
                  $resultannekardesi = $baglanti->query($sqlannekardesi);
                  $sqlannebabasi = "SELECT * FROM `101m` WHERE `TC` = '" . $row["BABATC"] ."' ";
                  $resultannebabasi = $baglanti->query($sqlannebabasi);
                  $sqlanneanasi = "SELECT * FROM `101m` WHERE `TC` = '" . $row["ANNETC"] ."' ";
                  $resultanneanasi = $baglanti->query($sqlanneanasi);
  
                  while($row = $resultannekardesi->fetch_assoc()) {
                    $response[] = array(
                        "YAKINLIK" => "DAYI/TEYZE",
                        "TC" => $row["TC"],
                        "ADI" => $row["ADI"],
                        "SOYADI" => $row["SOYADI"],
                        "DOGUMTARIHI" => $row["DOGUMTARIHI"],
                        "ANNEADI" => $row["ANNEADI"],
                        "ANNETC" => $row["ANNETC"],
                        "BABAADI" => $row["BABAADI"],
                        "BABATC" => $row["BABATC"],
                        "NUFUSIL" => $row["NUFUSIL"],
                        "NUFUSILCE" => $row["NUFUSILCE"]
                    );
                      $sqlannekardescocugu = "SELECT * FROM `101m` WHERE `BABATC` = '" . $row["TC"] ."' OR `ANNETC` = '" . $row["TC"] ."' ";
                      $resultannekardescocugu = $baglanti->query($sqlannekardescocugu);
                      while($row = $resultannekardescocugu->fetch_assoc()) {
                        $response[] = array(
                            "YAKINLIK" => "ANNE TARAFI KUZENİ",
                            "TC" => $row["TC"],
                            "ADI" => $row["ADI"],
                            "SOYADI" => $row["SOYADI"],
                            "DOGUMTARIHI" => $row["DOGUMTARIHI"],
                            "ANNEADI" => $row["ANNEADI"],
                            "ANNETC" => $row["ANNETC"],
                            "BABAADI" => $row["BABAADI"],
                            "BABATC" => $row["BABATC"],
                            "NUFUSIL" => $row["NUFUSIL"],
                            "NUFUSILCE" => $row["NUFUSILCE"]
                        );
                          $sqlannekardesannekardescocugu = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["TC"] ."' OR `ANNETC` = '" . $row["TC"] ."' ) ";
                          $resultannekardesannekardescocugu = $baglanti->query($sqlannekardesannekardescocugu);    
                          while($row = $resultannekardesannekardescocugu->fetch_assoc()) {
                             
                              $sqlannekardesannekardesannekardescocugu = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["TC"] ."' OR `ANNETC` = '" . $row["TC"] ."' ) ";
                              $resultannekardesannekardesannekardescocugu = $baglanti->query($sqlannekardesannekardesannekardescocugu);    
                              while($row = $resultannekardesannekardesannekardescocugu->fetch_assoc()) {
                                 
                                  
                              }
                          }

                      }
                  }
      
                  while($row = $resultannebabasi->fetch_assoc()) {
                    $response[] = array(
                        "YAKINLIK" => "DEDESİ",
                        "TC" => $row["TC"],
                        "ADI" => $row["ADI"],
                        "SOYADI" => $row["SOYADI"],
                        "DOGUMTARIHI" => $row["DOGUMTARIHI"],
                        "ANNEADI" => $row["ANNEADI"],
                        "ANNETC" => $row["ANNETC"],
                        "BABAADI" => $row["BABAADI"],
                        "BABATC" => $row["BABATC"],
                        "NUFUSIL" => $row["NUFUSIL"],
                        "NUFUSILCE" => $row["NUFUSILCE"]
                    );
                      $sqlbabakardesi = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["BABATC"] ."' OR `ANNETC` = '" . $row["ANNETC"] ."' ) ";
                      $resultbabakardesi = $baglanti->query($sqlbabakardesi);
                      $sqlbabababasi = "SELECT * FROM `101m` WHERE `TC` = '" . $row["BABATC"] ."' ";
                      $resultbabababasi = $baglanti->query($sqlbabababasi);
                      $sqlbabaanasi = "SELECT * FROM `101m` WHERE `TC` = '" . $row["ANNETC"] ."' ";
                      $resultbabaanasi = $baglanti->query($sqlbabaanasi);
      
                      while($row = $resultbabakardesi->fetch_assoc()) {
                         
                          $sqlannebabakardescocugu = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["TC"] ."' OR `ANNETC` = '" . $row["TC"] ."' ) ";
                          $resultannebabakardescocugu = $baglanti->query($sqlannebabakardescocugu);
                          while($row = $resultannebabakardescocugu->fetch_assoc()) {
                             
                              $sqlannebabakardesannebabakardescocugu = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["TC"] ."' OR `ANNETC` = '" . $row["TC"] ."' ) ";
                              $resultannebabakardesannebabakardescocugu = $baglanti->query($sqlannebabakardesannebabakardescocugu);    
                              while($row = $resultannebabakardesannebabakardescocugu->fetch_assoc()) {
                                 
                                  $sqlannebabakardesannebabakardesannebabakardescocugu = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["TC"] ."' OR `ANNETC` = '" . $row["TC"] ."' ) ";
                                  $resultannebabakardesannebabakardesannebabakardescocugu = $baglanti->query($sqlannebabakardesannebabakardesannebabakardescocugu);    
                                  while($row = $resultannebabakardesannebabakardesannebabakardescocugu->fetch_assoc()) {
                                    
                                  }
                              }

                          }
                      }
          
                      while($row = $resultbabababasi->fetch_assoc()) {
                        
                          
                      }
                      while($row = $resultbabaanasi->fetch_assoc()) {
                          
                          
                      }
                  }
                  while($row = $resultanneanasi->fetch_assoc()) {
                    $response[] = array(
                        "YAKINLIK" => "ANNEANNESİ",
                        "TC" => $row["TC"],
                        "ADI" => $row["ADI"],
                        "SOYADI" => $row["SOYADI"],
                        "DOGUMTARIHI" => $row["DOGUMTARIHI"],
                        "ANNEADI" => $row["ANNEADI"],
                        "ANNETC" => $row["ANNETC"],
                        "BABAADI" => $row["BABAADI"],
                        "BABATC" => $row["BABATC"],
                        "NUFUSIL" => $row["NUFUSIL"],
                        "NUFUSILCE" => $row["NUFUSILCE"]
                    );
                      $sqlannekardesi = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["BABATC"] ."' OR `ANNETC` = '" . $row["ANNETC"] ."' ) ";
                      $resultannekardesi = $baglanti->query($sqlannekardesi);
                      $sqlannebabasi = "SELECT * FROM `101m` WHERE `TC` = '" . $row["BABATC"] ."' ";
                      $resultannebabasi = $baglanti->query($sqlannebabasi);
                      $sqlanneanasi = "SELECT * FROM `101m` WHERE `TC` = '" . $row["ANNETC"] ."' ";
                      $resultanneanasi = $baglanti->query($sqlanneanasi);
      
                      while($row = $resultannekardesi->fetch_assoc()) {
                         
                          $sqlanneannekardescocugu = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["TC"] ."' OR `ANNETC` = '" . $row["TC"] ."' ) ";
                          $resultanneannekardescocugu = $baglanti->query($sqlanneannekardescocugu);
                          while($row = $resultanneannekardescocugu->fetch_assoc()) {
                             
                              $sqlanneannekardesanneannekardescocugu = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["TC"] ."' OR `ANNETC` = '" . $row["TC"] ."' ) ";
                              $resultanneannekardesanneannekardescocugu = $baglanti->query($sqlanneannekardesanneannekardescocugu);    
                              while($row = $resultanneannekardesanneannekardescocugu->fetch_assoc()) {
                               
                                  $sqlanneannekardesanneannekardesanneannekardescocugu = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["TC"] ."' OR `ANNETC` = '" . $row["TC"] ."' ) ";
                                  $resultanneannekardesanneannekardesanneannekardescocugu = $baglanti->query($sqlanneannekardesanneannekardesanneannekardescocugu);    
                                  while($row = $resultanneannekardesanneannekardesanneannekardescocugu->fetch_assoc()) {
                                      
                                      $sqlanneannekardesanneannekardesanneannekardesanneannekardescocugu = "SELECT * FROM `101m` WHERE NOT `TC` = '". $row["TC"] ."'  AND (`BABATC` = '" . $row["TC"] ."' OR `ANNETC` = '" . $row["TC"] ."' ) ";
                                      $resultanneannekardesanneannekardesanneannekardesanneannekardescocugu = $baglanti->query($sqlanneannekardesanneannekardesanneannekardesanneannekardescocugu);    
                                      while($row = $resultanneannekardesanneannekardesanneannekardesanneannekardescocugu->fetch_assoc()) {
                                         
                                  }

                              }
                          }

                      }
          
                      while($row = $resultannebabasi->fetch_assoc()) {
                          
                      }
                      while($row = $resultanneanasi->fetch_assoc()) {
                         
                      }
                      }
                  }
  
              }
              echo json_encode(array("coder:ahmwt.wip" ,"success" => true, "data" => $response),  JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);

            }
        }
      
          ?>