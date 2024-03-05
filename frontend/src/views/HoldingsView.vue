<template>
  <div class="container-fluid py-4">
    <div class="row">
      <div class="col-12">
        <div class="card my-4">
          <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2">
            <div class="bg-gradient-primary shadow-primary border-radius-lg pt-4 pb-3">
              <div class="row">
                <div class="col-6 d-flex align-items-center">
                  <h6 class="text-white text-capitalize ps-3">Holdings</h6>
                </div>
                <div class="col-6 text-end">
                  <a class="btn btn-success" href="javascript:;"><i class="material-icons text-sm">add</i>&nbsp;&nbsp;Add New Crypto</a>
                </div>
              </div>
            </div>
          </div>
          <div class="card-body px-0 pb-2">
            <div class="table-responsive p-0">
              <table class="table align-items-center mb-0">
                <thead>
                  <tr>
                    <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">Asset</th>
                    <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7 ps-2">Units</th>
                    <th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">EUR Value</th>
                    <th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">24h change</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>
                      <div class="d-flex px-2 py-1">
                        <div>
                          <img src="./assets/img/icon/btc.svg" class="avatar avatar-sm me-3" alt="xd">
                        </div>
                        <div class="d-flex flex-column justify-content-center">
                          <h6 class="mb-0 text-sm">Bitcoin(BTC)</h6>
                        </div>
                      </div>
                    </td>
                    <td class="align-middle  text-sm">
                      <span class="text-xs font-weight-bold"> 0.12302 </span>
                    </td>
                    <td class="align-middle text-center text-sm">
                      <span class="text-xs font-weight-bold"> €14,000 </span>
                    </td>
                    <td class="align-middle text-center">
                      <span class="text-danger text-sm font-weight-bolder">-2%</span>
                    </td>
                  </tr>
                  <tr>
                    <td>
                      <div class="d-flex px-2 py-1">
                        <div>
                          <img src="./assets/img/icon/eth.svg" class="avatar avatar-sm me-3" alt="xd">
                        </div>
                        <div class="d-flex flex-column justify-content-center">
                          <h6 class="mb-0 text-sm">Ethereum(ETH)</h6>
                        </div>
                      </div>
                    </td>
                    <td class="align-middle  text-sm">
                      <span class="text-xs font-weight-bold"> 1.3 </span>
                    </td>
                    <td class="align-middle text-center text-sm">
                      <span class="text-xs font-weight-bold"> €3,778.05 </span>
                    </td>
                    <td class="align-middle text-center">
                      <span class="text-danger text-sm font-weight-bolder">-2%</span>
                    </td>
                  </tr>
                  <tr>
                    <td>
                      <div class="d-flex px-2 py-1">
                        <div>
                          <img src="./assets/img/icon/xmr.svg" class="avatar avatar-sm me-3" alt="xd">
                        </div>
                        <div class="d-flex flex-column justify-content-center">
                          <h6 class="mb-0 text-sm">Monero(XMR)</h6>
                        </div>
                      </div>
                    </td>
                    <td class="align-middle  text-sm">
                      <span class="text-xs font-weight-bold"> 120.04 </span>
                    </td>
                    <td class="align-middle text-center text-sm">
                      <span class="text-xs font-weight-bold"> €143.55 </span>
                    </td>
                    <td class="align-middle text-center">
                      <span class="text-danger text-sm font-weight-bolder">-2%</span>
                    </td>
                  </tr>
                  <tr>
                    <td>
                      <div class="d-flex px-2 py-1">
                        <div>
                          <img src="./assets/img/icon/ada.svg" class="avatar avatar-sm me-3" alt="xd">
                        </div>
                        <div class="d-flex flex-column justify-content-center">
                          <h6 class="mb-0 text-sm">Cardano(ADA)</h6>
                        </div>
                      </div>
                    </td>
                    <td class="align-middle  text-sm">
                      <span class="text-xs font-weight-bold"> 0.12302 </span>
                    </td>
                    <td class="align-middle text-center text-sm">
                      <span class="text-xs font-weight-bold"> €137.00 </span>
                    </td>
                    <td class="align-middle text-center">
                      <span class="text-danger text-sm font-weight-bolder">-2%</span>
                    </td>
                  </tr>
                  <tr>
                    <td>
                      <div class="d-flex px-2 py-1">
                        <div>
                          <img src="./assets/img/icon/link.svg" class="avatar avatar-sm me-3" alt="xd">
                        </div>
                        <div class="d-flex flex-column justify-content-center">
                          <h6 class="mb-0 text-sm">Chainlink(LINK)</h6>
                        </div>
                      </div>
                    </td>
                    <td class="align-middle  text-sm">
                      <span class="text-xs font-weight-bold"> 22 </span>
                    </td>
                    <td class="align-middle text-center text-sm">
                      <span class="text-xs font-weight-bold"> €123.33 </span>
                    </td>
                    <td class="align-middle text-center">
                      <span class="text-danger text-sm font-weight-bolder">-2%</span>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>